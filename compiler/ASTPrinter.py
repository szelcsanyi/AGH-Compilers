from dataclasses import dataclass
from typing import List, Tuple

from colored import stylize, fg
from tree_format import format_tree

from compiler import AST
from compiler.utils import method_dispatch


@dataclass
class TmpNode(AST.Node):
    name: str
    children: List[AST.Node]


class ASTPrinter:

    def generate(self, root: AST.Node) -> str:
        """ Generates string representation of given AST tree """
        return format_tree(
            root,
            self._format_name,
            self._format_children
        )

    def _format_name(self, node: AST.Node) -> str:
        return "{} {}".format(
            self._get_name(node),
            stylize(f' [{node.line_span[0]}-{node.line_span[1]}]', fg('grey_23'))
        )

    def _format_children(self, node: AST.Node) -> List[AST.Node]:
        return self._get_children(node)

    # ==============================================
    #   GET NODE NAME
    # ==============================================
    @method_dispatch
    def _get_name(self, node: AST.Node) -> str:
        raise NotImplementedError(f'There is no tree generator implemented for {node.__class__}')

    @_get_name.register
    def _(self, node: AST.ConstantExpression) -> str:
        return str(node.value)

    @_get_name.register
    def _(self, node: AST.VectorExpression) -> str:
        return 'VECTOR'

    @_get_name.register
    def _(self, node: AST.RangeExpression) -> str:
        return 'RANGE'

    @_get_name.register
    def _(self, node: AST.ScalarOperatorExpression) -> str:
        return node.operator

    @_get_name.register
    def _(self, node: AST.EqualOperatorExpression) -> str:
        return node.operator

    @_get_name.register
    def _(self, node: AST.MatrixOperatorExpression) -> str:
        return node.operator

    @_get_name.register
    def _(self, node: AST.TransposeExpression) -> str:
        return 'TRANSPOSE'

    @_get_name.register
    def _(self, node: AST.UnaryMinusExpression) -> str:
        return '-'

    @_get_name.register
    def _(self, node: AST.FunctionExpression) -> str:
        return node.name

    @_get_name.register
    def _(self, node: AST.Identifier) -> str:
        return node.name

    @_get_name.register
    def _(self, node: AST.Selector) -> str:
        return node.identifier.name

    @_get_name.register
    def _(self, node: AST.ProgramStatement) -> str:
        return '┐'

    @_get_name.register
    def _(self, node: AST.AssignmentStatement) -> str:
        return '='

    @_get_name.register
    def _(self, node: AST.AssignmentWithOperatorStatement) -> str:
        return node.operator

    @_get_name.register
    def _(self, node: AST.InstructionStatement) -> str:
        return node.name

    @_get_name.register
    def _(self, node: AST.WhileStatement) -> str:
        return 'WHILE'

    @_get_name.register
    def _(self, node: AST.ForStatement) -> str:
        return 'FOR'

    @_get_name.register
    def _(self, node: AST.IfStatement) -> str:
        return 'IF'

    @_get_name.register
    def _(self, node: TmpNode) -> str:
        return node.name

    # ==============================================
    #   GET NODE CHILDREN
    # ==============================================
    @method_dispatch
    def _get_children(self, node: AST.Node) -> List[AST.Node]:
        raise NotImplementedError(f'There is no tree generator implemented for {node.__class__}')

    @_get_children.register
    def _(self, node: AST.ConstantExpression) -> List[AST.Node]:
        return []

    @_get_children.register
    def _(self, node: AST.VectorExpression) -> List[AST.Node]:
        return node.expressions

    @_get_children.register
    def _(self, node: AST.RangeExpression) -> List[AST.Node]:
        return [node.begin, node.end]

    @_get_children.register
    def _(self, node: AST.ScalarOperatorExpression) -> List[AST.Node]:
        return node.expressions

    @_get_children.register
    def _(self, node: AST.EqualOperatorExpression) -> List[AST.Node]:
        return [node.left_expression, node.right_expression]

    @_get_children.register
    def _(self, node: AST.MatrixOperatorExpression) -> List[AST.Node]:
        return [node.left_expression, node.right_expression]

    @_get_children.register
    def _(self, node: AST.TransposeExpression) -> List[AST.Node]:
        return [node.expression]

    @_get_children.register
    def _(self, node: AST.UnaryMinusExpression) -> List[AST.Node]:
        return [node.expression]

    @_get_children.register
    def _(self, node: AST.FunctionExpression) -> List[AST.Node]:
        return node.arguments

    @_get_children.register
    def _(self, node: AST.Identifier) -> List[AST.Node]:
        return []

    @_get_children.register
    def _(self, node: AST.Selector) -> List[AST.Node]:
        return [TmpNode(node.selector.line_span, 'SELECTOR', node.selector.expressions)]

    @_get_children.register
    def _(self, node: AST.ProgramStatement) -> List[AST.Node]:
        return node.statements

    @_get_children.register
    def _(self, node: AST.AssignmentStatement) -> List[AST.Node]:
        return [node.variable, node.expression]

    @_get_children.register
    def _(self, node: AST.AssignmentWithOperatorStatement) -> List[AST.Node]:
        return [node.variable, node.expression]

    @_get_children.register
    def _(self, node: AST.InstructionStatement) -> List[AST.Node]:
        return node.arguments

    @_get_children.register
    def _(self, node: AST.WhileStatement) -> List[AST.Node]:
        return [node.condition, node.statement]

    @_get_children.register
    def _(self, node: AST.ForStatement) -> List[AST.Node]:
        return [node.identifier, node.range, node.statement]

    @_get_children.register
    def _(self, node: AST.IfStatement) -> List[AST.Node]:
        children = [node.condition, TmpNode(node.statement_then.line_span, 'THEN', [node.statement_then])]
        if node.statement_else:
            children += [TmpNode(node.statement_else.line_span, 'ELSE', [node.statement_else])]
        return children

    @_get_children.register
    def _(self, node: TmpNode) -> List[AST.Node]:
        return node.children
