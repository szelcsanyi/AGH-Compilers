from typing import Any, Tuple

import numpy as np

from compiler.interpreter.interuptions import BreakInterruption, ContinueInterruption, ReturnInterruption
from compiler.interpreter.operations import OPERATIONS
from compiler.parser import AST
from compiler.utils import SymbolTable, method_dispatch, CompilerError


class Interpreter:
    """ Class responsible for executing code provided in form of AST tree """

    def __init__(self):
        self.memory = SymbolTable()

    def execute_with_return(self, node: AST.Node):
        """ Executes given AST tree and catches return interruption """
        try:
            return self.execute(node)
        except ReturnInterruption as err:
            return err.value

    @method_dispatch
    def execute(self, node: AST.Node) -> Any:
        """ Executes given AST tree """
        raise NotImplementedError(f'There is no execution implemented for {node.__class__}')

    # ==============================================
    #   EXPRESSIONS
    # ==============================================
    @execute.register
    def _(self, node: AST.ConstantExpression) -> Any:
        return node.value

    @execute.register
    def _(self, node: AST.VectorExpression) -> np.ndarray:
        return np.asarray([self.execute(e) for e in node.expressions])

    @execute.register
    def _(self, node: AST.RangeExpression) -> range:
        return range(self.execute(node.begin), self.execute(node.end))

    @execute.register
    def _(self, node: AST.OperatorExpression) -> Any:
        args = [self.execute(a) for a in node.expressions]
        return OPERATIONS[node.operator](*args)

    @execute.register
    def _(self, node: AST.FunctionExpression) -> Any:
        args = [self.execute(a) for a in node.arguments]
        return OPERATIONS[node.name](*args)

    # ==============================================
    #   VARIABLES
    # ==============================================
    @execute.register
    def _(self, node: AST.Identifier) -> Any:
        return self.memory[node.name]

    @execute.register
    def _(self, node: AST.Selector) -> Any:
        var = self.execute(node.identifier)
        sel = self.execute(node.selector)

        return var[tuple(sel)]

    # ==============================================
    #   STATEMENTS
    # ==============================================
    @execute.register
    def _(self, node: AST.ProgramStatement) -> None:
        with self.memory.context_scope('program'):
            for s in node.statements:
                self.execute(s)

    @execute.register
    def _(self, node: AST.AssignmentStatement) -> None:

        # if its an assignment to identifier
        if isinstance(node.variable, AST.Identifier):
            self.memory[node.variable.name] = self.execute(node.expression)

        # if its an assignment to selector
        if isinstance(node.variable, AST.Selector):
            var = self.execute(node.variable.identifier)
            sel = self.execute(node.variable.selector)
            exp = self.execute(node.expression)

            var[tuple(sel)] = exp

    @execute.register
    def _(self, node: AST.AssignmentWithOperatorStatement) -> None:
        exp = self.execute(node.expression)

        # if its an assignment to identifier
        if isinstance(node.variable, AST.Identifier):
            var = self.execute(node.variable)

            self.memory[node.variable.name] = OPERATIONS[node.operator[:1]](var, exp)

        # if its an assignment to selector
        if isinstance(node.variable, AST.Selector):
            var = self.execute(node.variable.identifier)
            sel = tuple(self.execute(node.variable.selector))

            var[sel] = OPERATIONS[node.operator[:1]](var[sel], exp)

    @execute.register
    def _(self, node: AST.InstructionStatement) -> None:
        args = [self.execute(a) for a in node.arguments]
        return OPERATIONS[node.name](*args)

    @execute.register
    def _(self, node: AST.WhileStatement) -> None:
        while self.execute(node.condition):
            with self.memory.context_scope('while'):
                try:
                    self.execute(node.statement)
                except BreakInterruption:
                    return
                except ContinueInterruption:
                    pass

    @execute.register
    def _(self, node: AST.ForStatement) -> None:
        for i in self.execute(node.range):
            with self.memory.context_scope('for'):
                self.memory[node.identifier.name] = i
                try:
                    self.execute(node.statement)
                except BreakInterruption:
                    return
                except ContinueInterruption:
                    pass

    @execute.register
    def _(self, node: AST.IfStatement) -> None:
        if self.execute(node.condition):
            with self.memory.context_scope('then'):
                self.execute(node.statement_then)

        elif node.statement_else:
            with self.memory.context_scope('else'):
                self.execute(node.statement_else)


class ExecutionError(CompilerError):
    def __init__(self, line_span: Tuple[int, int], msg: str) -> None:
        super().__init__('Interpreter', line_span[0], msg)

        self.line_span = line_span
