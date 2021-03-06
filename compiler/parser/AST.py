from abc import ABC
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple


# ==============================================
#   ABSTRACT
# ==============================================
@dataclass
class Node(ABC):
    line_span: Tuple[int, int]


class Expression(Node):
    pass


class Statement(Node):
    pass


class Variable(Node):
    pass


# ==============================================
#   EXPRESSIONS
# ==============================================
@dataclass
class ConstantExpression(Expression):
    value: Any


@dataclass
class VectorExpression(Expression):
    expressions: List[Expression]


@dataclass
class RangeExpression(Expression):
    begin: Expression
    end: Expression


@dataclass
class OperatorExpression(Expression):
    operator: str
    expressions: List[Expression]


@dataclass
class FunctionExpression(Expression):
    name: str
    arguments: List[Expression]


# ==============================================
#   VARIABLE
# ==============================================
@dataclass
class Identifier(Variable):
    name: str


@dataclass
class Selector(Variable):
    identifier: Identifier
    selector: VectorExpression


# ==============================================
#   STATEMENTS
# ==============================================
@dataclass
class ProgramStatement(Statement):
    statements: List[Statement]


@dataclass
class AssignmentStatement(Statement):
    variable: Variable
    expression: Expression


@dataclass
class AssignmentWithOperatorStatement(Statement):
    operator: str
    variable: Variable
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
    identifier: Identifier
    range: RangeExpression
    statement: Statement


@dataclass
class IfStatement(Statement):
    condition: Expression
    statement_then: Statement
    statement_else: Optional[Statement]
