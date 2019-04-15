from abc import ABC


class Node(ABC):
    def __init__(self, production):
        self.linespan = production.linespan(0)


class ProgramStatement(Node):
    def __init__(self, production, *statements):
        super().__init__(production)

        self.statements = statements


class AssignmentStatement(Node):
    def __init__(self, production, operator, variable, expression):
        super().__init__(production)

        self.operator = operator
        self.variable = variable
        self.expression = expression


class InstructionStatement(Node):
    def __init__(self, production, name, *arguments):
        super().__init__(production)

        self.name = name
        self.arguments = arguments


class WhileStatement(Node):
    def __init__(self, production, condition, statement):
        super().__init__(production)

        self.condition = condition
        self.statement = statement


class ForStatement(Node):
    def __init__(self, production, identifier, range, statement):
        super().__init__(production)

        self.identifier = identifier
        self.range = range
        self.statement = statement


class IfStatement(Node):
    def __init__(self, production, condition, statement_then, statement_else=None):
        super().__init__(production)

        self.condition = condition
        self.statement_then = statement_then
        self.statement_else = statement_else


class OperatorExpression(Node):
    def __init__(self, production, operator, *expressions):
        super().__init__(production)

        self.operator = operator
        self.expressions = expressions


class ConstantExpression(Node):
    def __init__(self, production, value):
        super().__init__(production)

        self.value = value


class FunctionExpression(Node):
    def __init__(self, production, name, *arguments):
        super().__init__(production)

        self.name = name
        self.arguments = arguments


class Identifier(Node):
    def __init__(self, production, name):
        super().__init__(production)

        self.name = name


class Selector(Node):
    def __init__(self, production, expression, vector):
        super().__init__(production)

        self.expression = expression
        self.vector = vector


class RangeExpression(Node):
    def __init__(self, production, begin, end):
        super().__init__(production)

        self.begin = begin
        self.end = end


class VectorExpression(Node):
    def __init__(self, production, *expressions):
        super().__init__(production)

        self.expressions = expressions
