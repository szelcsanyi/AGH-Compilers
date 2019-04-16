from tree_format import format_tree
from colored import stylize, fg

from compiler import AST


def get_ast_tree(root: AST.Node):
    return format_tree(
        root,
        lambda n: n.get_ast_name() + stylize(f' [{n.production.linespan(0)[0]}-{n.production.linespan(0)[1]}]', fg('grey_23')),
        lambda n: n.get_ast_children()
    )


def add_to_class(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TmpNode:
    def __init__(self, name, *children):
        self.name = name
        self.children = children
        self.production = children[0].production

    def get_ast_name(self):
        return self.name

    def get_ast_children(self):
        return self.children


@add_to_class(AST.ProgramStatement)
def get_ast_name(self):
    return '┐'


@add_to_class(AST.ProgramStatement)
def get_ast_children(self):
    return self.statements


@add_to_class(AST.AssignmentStatement)
def get_ast_name(self):
    return self.operator


@add_to_class(AST.AssignmentStatement)
def get_ast_children(self):
    return [self.variable, self.expression]


@add_to_class(AST.InstructionStatement)
def get_ast_name(self):
    return self.name


@add_to_class(AST.InstructionStatement)
def get_ast_children(self):
    return self.arguments


@add_to_class(AST.WhileStatement)
def get_ast_name(self):
    return 'WHILE'


@add_to_class(AST.WhileStatement)
def get_ast_children(self):
    return [self.condition, self.statement]


@add_to_class(AST.ForStatement)
def get_ast_name(self):
    return 'FOR'


@add_to_class(AST.ForStatement)
def get_ast_children(self):
    return [self.identifier, self.range, self.statement]


@add_to_class(AST.IfStatement)
def get_ast_name(self):
    return 'IF'


@add_to_class(AST.IfStatement)
def get_ast_children(self):
    return [self.condition, TmpNode('THEN', self.statement_then)] + [TmpNode('ELSE', self.statement_else)] if self.statement_else else []


@add_to_class(AST.OperatorExpression)
def get_ast_name(self):
    return self.operator


@add_to_class(AST.OperatorExpression)
def get_ast_children(self):
    return self.expressions


@add_to_class(AST.ConstantExpression)
def get_ast_name(self):
    return str(self.value)


@add_to_class(AST.ConstantExpression)
def get_ast_children(self):
    return []


@add_to_class(AST.FunctionExpression)
def get_ast_name(self):
    return self.name


@add_to_class(AST.FunctionExpression)
def get_ast_children(self):
    return self.arguments


@add_to_class(AST.IdentifierExpression)
def get_ast_name(self):
    return self.name


@add_to_class(AST.IdentifierExpression)
def get_ast_children(self):
    return []


@add_to_class(AST.SelectorExpression)
def get_ast_name(self):
    return 'SELECTOR'


@add_to_class(AST.SelectorExpression)
def get_ast_children(self):
    return [self.expression, self.vector]


@add_to_class(AST.RangeExpression)
def get_ast_name(self):
    return 'RANGE'


@add_to_class(AST.RangeExpression)
def get_ast_children(self):
    return [self.begin, self.end]


@add_to_class(AST.VectorExpression)
def get_ast_name(self):
    return 'VECTOR'


@add_to_class(AST.VectorExpression)
def get_ast_children(self):
    return self.expressions
