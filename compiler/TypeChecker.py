""" Type checker module """
from typing import Tuple

from compiler import AST, SymbolTable
from compiler.utils import method_dispatch


class TypeChecker:

    def __init__(self, symbol_table: SymbolTable = SymbolTable()):
        self.symbol_table = symbol_table
        self.errors = []

    def _error(self, line_span: Tuple[int, int], message: str):
        self.errors.append((line_span, message))

    def print_errors(self):
        for lines, msg in self.errors:
            print(f"Type error at line {lines[0]}: {msg}")

    @method_dispatch
    def check(self, node: AST.Node):
        raise NotImplementedError(f'There is no type check implemented for {node.__class__}')

    # ==============================================
    #   EXPRESSIONS
    # ==============================================
    @check.register
    def _(self, node: AST.ConstantExpression):
        raise NotImplementedError('type check for ConstantExpression')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.VectorExpression):
        raise NotImplementedError('type check for VectorExpression')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.RangeExpression):
        raise NotImplementedError('type check for RangeExpression')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.ScalarOperatorExpression):
        raise NotImplementedError('type check for ScalarOperatorExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.EqualOperatorExpression):
        raise NotImplementedError('type check for EqualOperatorExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.MatrixOperatorExpression):
        raise NotImplementedError('type check for MatrixOperatorExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.TransposeExpression):
        raise NotImplementedError('type check for TransposeExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.UnaryMinusExpression):
        raise NotImplementedError('type check for UnaryMinusExpression')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.FunctionExpression):
        raise NotImplementedError('type check for FunctionExpression')  # TODO: Implement

    # ==============================================
    #   VARIABLES
    # ==============================================
    @check.register
    def _(self, node: AST.Identifier):
        raise NotImplementedError('type check for Identifier')  # TODO: Implement

    @check.register
    def _(self, node: AST.Selector):
        raise NotImplementedError('type check for Selector')  # TODO: Implement

    # ==============================================
    #   STATEMENTS
    # ==============================================
    @check.register
    def _(self, node: AST.ProgramStatement):
        for statement in node.statements:
            self.check(statement)
    
    @check.register
    def _(self, node: AST.AssignmentStatement):
        raise NotImplementedError('type check for AssignmentStatement')  # TODO: Implement

    @check.register
    def _(self, node: AST.AssignmentWithOperatorStatement):
        raise NotImplementedError('type check for AssignmentWithOperatorStatement')  # TODO: Implement

    @check.register
    def _(self, node: AST.InstructionStatement):
        raise NotImplementedError('type check for InstructionStatement')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.WhileStatement):
        raise NotImplementedError('type check for WhileStatement')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.ForStatement):
        raise NotImplementedError('type check for ForStatement')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.IfStatement):
        raise NotImplementedError('type check for IfStatement')  # TODO: Implement
