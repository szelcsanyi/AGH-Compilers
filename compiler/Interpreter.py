""" Interpreter module """
from typing import Any, List, Tuple

from compiler import AST
from compiler.utils import method_dispatch


class Interpreter:

    @method_dispatch
    def execute(self, node: AST.Node) -> Any:
        raise NotImplementedError(f'There is no execution implemented for {node.__class__}')

    # ==============================================
    #   EXPRESSIONS
    # ==============================================
    @execute.register
    def _(self, node: AST.ConstantExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.VectorExpression) -> List[Any]:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.RangeExpression) -> Tuple[Any, Any]:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.ScalarOperatorExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.EqualOperatorExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.MatrixOperatorExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.TransposeExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.UnaryMinusExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.FunctionExpression) -> Any:
        raise NotImplementedError()  # TODO: Implement

    # ==============================================
    #   VARIABLES
    # ==============================================
    @execute.register
    def _(self, node: AST.Identifier) -> Any:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.Selector) -> Any:
        raise NotImplementedError()  # TODO: Implement

    # ==============================================
    #   STATEMENTS
    # ==============================================
    @execute.register
    def _(self, node: AST.ProgramStatement) -> None:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.AssignmentStatement) -> None:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.AssignmentWithOperatorStatement) -> None:
        raise NotImplementedError()  # TODO: Implement

    @execute.register
    def _(self, node: AST.InstructionStatement) -> None:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.WhileStatement) -> None:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.ForStatement) -> None:
        raise NotImplementedError()  # TODO: Implement
    
    @execute.register
    def _(self, node: AST.IfStatement) -> None:
        raise NotImplementedError()  # TODO: Implement
