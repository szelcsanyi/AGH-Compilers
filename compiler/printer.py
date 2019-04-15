from tree_format import format_tree
from colored import stylize, fg

from compiler import AST


def get_ast_tree(root):
    return format_tree(
        root,
        lambda n: n.get_ast_name() + stylize(f' [{n.linespan[0]}-{n.linespan[1]}]', fg('grey_23')),
        lambda n: n.get_ast_children()
    )


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


@addToClass(AST.ProgramStatement)
def get_ast_name(self):
    return '┐'


@addToClass(AST.ProgramStatement)
def get_ast_children(self):
    return self.statements


@addToClass(AST.AssignmentStatement)
def get_ast_name(self):
    return self.operator


@addToClass(AST.AssignmentStatement)
def get_ast_children(self):
    return [self.variable, self.expression]


@addToClass(AST.InstructionStatement)
def get_ast_name(self):
    return self.name


@addToClass(AST.InstructionStatement)
def get_ast_children(self):
    return self.arguments


@addToClass(AST.WhileStatement)
def get_ast_name(self):
    return 'WHILE'


@addToClass(AST.WhileStatement)
def get_ast_children(self):
    return [self.condition, self.statement]


@addToClass(AST.ForStatement)
def get_ast_name(self):
    return 'FOR'


@addToClass(AST.ForStatement)
def get_ast_children(self):
    return [self.identifier, self.range, self.statement]


@addToClass(AST.IfStatement)
def get_ast_name(self):
    return 'IF'


@addToClass(AST.IfStatement)
def get_ast_children(self):
    return [self.condition, self.statement_then] + [self.statement_else] if self.statement_else else []


@addToClass(AST.OperatorExpression)
def get_ast_name(self):
    return self.operator


@addToClass(AST.OperatorExpression)
def get_ast_children(self):
    return self.expressions


@addToClass(AST.ConstantExpression)
def get_ast_name(self):
    return str(self.value)


@addToClass(AST.ConstantExpression)
def get_ast_children(self):
    return []


@addToClass(AST.FunctionExpression)
def get_ast_name(self):
    return self.name


@addToClass(AST.FunctionExpression)
def get_ast_children(self):
    return self.arguments


@addToClass(AST.Identifier)
def get_ast_name(self):
    return self.name


@addToClass(AST.Identifier)
def get_ast_children(self):
    return []


@addToClass(AST.Selector)
def get_ast_name(self):
    return 'SELECTOR'


@addToClass(AST.Selector)
def get_ast_children(self):
    return [self.expression, self.vector]


@addToClass(AST.RangeExpression)
def get_ast_name(self):
    return 'RANGE'


@addToClass(AST.RangeExpression)
def get_ast_children(self):
    return [self.begin, self.end]


@addToClass(AST.VectorExpression)
def get_ast_name(self):
    return 'VECTOR'


@addToClass(AST.VectorExpression)
def get_ast_children(self):
    return self.expressions
