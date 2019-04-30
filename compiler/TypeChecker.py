""" Type checker module """

from compiler import AST, SymbolTable
from compiler.utils import method_dispatch


class TypeChecker:

    def __init__(self, symbol_table: SymbolTable = SymbolTable()):
        self.symbol_table = symbol_table

    @method_dispatch
    def check(self, node: AST.Node):
        raise NotImplementedError(f'There is no type check implemented for {node.__class__}')

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
    def _(self, node: AST.OperatorExpression):
        raise NotImplementedError('type check for OperatorExpression')  # TODO: Implement
    
    @check.register
    def _(self, node: AST.FunctionExpression):
        raise NotImplementedError('type check for FunctionExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.Variable):
        raise NotImplementedError('type check for SelectorExpression')  # TODO: Implement

    @check.register
    def _(self, node: AST.ProgramStatement):
        for statement in node.statements:
            self.check(statement)
    
    @check.register
    def _(self, node: AST.AssignmentStatement):
        raise NotImplementedError('type check for AssignmentStatement')  # TODO: Implement

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
