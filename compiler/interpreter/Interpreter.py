""" Interpreter module """
from typing import Any, Tuple

import numpy as np

from compiler.parser import AST
from compiler.interpreter.operations import OPERATIONS
from compiler.utils import method_dispatch, CompilerError, SymbolTable


class Interpreter:

    def __init__(self):
        self.memory = SymbolTable()

    @method_dispatch
    def execute(self, node: AST.Node) -> Any:
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
    def _(self, node: AST.ScalarOperatorExpression) -> Any:
        left = self.execute(node.left_expression)
        right = self.execute(node.right_expression)

        # handle string casting
        if node.operator == '+' and (left is str or right is str):
            left = str(left)
            right = str(right)

        return OPERATIONS[node.operator](left, right)

    @execute.register
    def _(self, node: AST.EqualOperatorExpression) -> Any:
        left = self.execute(node.left_expression)
        right = self.execute(node.right_expression)

        return OPERATIONS[node.operator](left, right)

    @execute.register
    def _(self, node: AST.MatrixOperatorExpression) -> np.ndarray:
        left = self.execute(node.left_expression)
        right = self.execute(node.right_expression)

        return OPERATIONS[node.operator](left, right)

    @execute.register
    def _(self, node: AST.TransposeExpression) -> np.ndarray:
        return np.transpose(self.execute(node.expression))

    @execute.register
    def _(self, node: AST.UnaryMinusExpression) -> Any:
        return -self.execute(node.expression)
    
    @execute.register
    def _(self, node: AST.FunctionExpression) -> Any:
        args = [self.execute(a) for a in node.arguments]

        # for 'zeros' and 'ones' args have to be in form of tuple
        if node.name in ['zeros', 'ones']:
            args = [tuple(args)]

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

        # if its an assignment to identifier save to memory
        if isinstance(node.variable, AST.Identifier):
            self.memory[node.variable.name] = self.execute(node.expression)

        # if its an assignment to selector check type compatibility
        if isinstance(node.variable, AST.Selector):
            var = self.execute(node.variable.identifier)
            sel = self.execute(node.variable.selector)
            exp = self.execute(node.expression)

            var[tuple(sel)] = exp

    @execute.register
    def _(self, node: AST.AssignmentWithOperatorStatement) -> None:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.InstructionStatement) -> None:
        args = [self.execute(a) for a in node.arguments]

        if node.name == 'break':
            raise BreakException()
        if node.name == 'continue':
            raise ContinueException()
        if node.name == 'return':
            raise ReturnException(args[0])
        if node.name == 'print':
            print(*args)

        raise ExecutionError(node.line_span, f'Unexpected instruction: {node.name}')
    
    @execute.register
    def _(self, node: AST.WhileStatement) -> None:
        while self.execute(node.condition):
            with self.memory.context_scope('while'):
                try:
                    self.execute(node.statement)
                except BreakException:
                    return
                except ContinueException:
                    pass
    
    @execute.register
    def _(self, node: AST.ForStatement) -> None:
        for i in self.execute(node.range):
            with self.memory.context_scope('for'):
                self.memory[node.identifier.name] = i
                try:
                    self.execute(node.statement)
                except BreakException:
                    return
                except ContinueException:
                    pass

    @execute.register
    def _(self, node: AST.IfStatement) -> None:
        if self.execute(node.condition):
            with self.memory.context_scope('then'):
                self.execute(node.statement_then)

        elif node.statement_else:
            with self.memory.context_scope('else'):
                self.execute(node.statement_else)


class ExecutionException(Exception):
    """ Base exception used for control flow """
    pass


class BreakException(ExecutionException):
    """ Control flow exception raised in case of break instruction """
    pass


class ContinueException(ExecutionException):
    """ Control flow exception raised in case of continue instruction """
    pass


class ReturnException(ExecutionException):
    """ Control flow exception raised is case of return instruction """
    def __init__(self, value: Any):
        self.value = value


class ExecutionError(CompilerError):
    def __init__(self, line_span: Tuple[int, int], msg: str) -> None:
        super().__init__('Interpreter', line_span[0], msg)

        self.line_span = line_span
