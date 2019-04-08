from abc import ABC


class Node(ABC):
    pass


class ProgramStatement(Node):
    def __init__(self, *statements):
        self.statements = statements


class AssignmentStatement(Node):
    def __init__(self, operator, variable, expression):
        self.operator = operator
        self.variable = variable
        self.expression = expression


class InstructionStatement(Node):
    def __init__(self, name, *arguments):
        self.name = name
        self.arguments = arguments


class WhileStatement(Node):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement


class ForStatement(Node):
    def __init__(self, identifier, range, statement):
        self.identifier = identifier
        self.range = range
        self.statement = statement


class IfStatement(Node):
    def __init__(self, condition, statement_then, statement_else=None):
        self.condition = condition
        self.statement_then = statement_then
        self.statement_else = statement_else


class OperatorExpression(Node):
    def __init__(self, operator, *expressions):
        self.operator = operator
        self.expressions = expressions


class ConstantExpression(Node):
    def __init__(self, value):
        self.value = value


class FunctionExpression(Node):
    def __init__(self, name, *arguments):
        self.name = name
        self.arguments = arguments


class Identifier(Node):
    def __init__(self, name):
        self.name = name


class Selector(Node):
    def __init__(self, expression, vector):
        self.expression = expression
        self.vector = vector


class RangeExpression(Node):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


class VectorExpression(Node):
    def __init__(self, *expressions):
        self.expressions = expressions
