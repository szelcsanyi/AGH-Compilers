from abc import ABC
from dataclasses import dataclass
from typing import Any, List

from ply.yacc import YaccProduction


# ==============================================
#   ABSTRACT
# ==============================================
@dataclass
class Node(ABC):
    production: YaccProduction


class Expression(Node):
    pass


class Statement(Node):
    pass


# ==============================================
#   EXPRESSIONS
# ==============================================
@dataclass
class ConstantExpression(Expression):
    value: Any


@dataclass
class IdentifierExpression(Expression):
    name: str


@dataclass
class VectorExpression(Expression):
    expressions: List[Expression]


@dataclass
class RangeExpression(Expression):
    begin: Expression
    end: Expression


@dataclass
class SelectorExpression(Expression):
    expression: Expression
    vector: VectorExpression


@dataclass
class OperatorExpression(Expression):
    operator: str
    expressions: List[Expression]


@dataclass
class FunctionExpression(Expression):
    name: str
    arguments: List[Expression]


# ==============================================
#   STATEMENTS
# ==============================================
@dataclass
class ProgramStatement(Statement):
    statements: List[Statement]


@dataclass
class AssignmentStatement(Statement):
    operator: str
    variable: IdentifierExpression
    expression: Expression


@dataclass
class InstructionStatement(Statement):
    name: str
    arguments: List[Expression]


@dataclass
class WhileStatement(Statement):
    condition: Expression
    statement: Statement


@dataclass
class ForStatement(Statement):
    identifier: IdentifierExpression
    range: RangeExpression
    statement: Statement


@dataclass
class IfStatement(Statement):
    condition: Expression
    statement_then: Statement
    statement_else: Statement
