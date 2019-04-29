""" Type checker module """

from compiler import AST
from compiler.visitor import Visitor

v = Visitor()


@v.handler(AST.ConstantExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.IdentifierExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.VectorExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.RangeExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.SelectorExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.OperatorExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.FunctionExpression)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.ProgramStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.AssignmentStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.InstructionStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.WhileStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.ForStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement


@v.handler(AST.IfStatement)
def visit(node):
    raise NotImplemented()  # TODO: Implement
