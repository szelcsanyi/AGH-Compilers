from operator import itemgetter

from tree_format import format_tree

from compiler import AST


def get_ast_tree(root):
    return format_tree(root.get_ast(), itemgetter(0), itemgetter(1))


def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


@addToClass(AST.ProgramStatement)
def get_ast(self):
    return '┐', [n.get_ast() for n in self.statements]


@addToClass(AST.AssignmentStatement)
def get_ast(self):
    return self.operator, [self.variable.get_ast(), self.expression.get_ast()]


@addToClass(AST.InstructionStatement)
def get_ast(self):
    return self.name, [n.get_ast() for n in self.arguments]


@addToClass(AST.WhileStatement)
def get_ast(self):
    return 'WHILE', [self.condition.get_ast(), self.statement.get_ast()]


@addToClass(AST.ForStatement)
def get_ast(self):
    return 'FOR', [self.identifier.get_ast(), self.range.get_ast(), self.statement.get_ast()]


@addToClass(AST.IfStatement)
def get_ast(self):
    return 'IF', [self.condition.get_ast(), ('THEN', [self.statement_then.get_ast()])] + [('ELSE', [self.statement_else.get_ast()])] if self.statement_else else []


@addToClass(AST.OperatorExpression)
def get_ast(self):
    return self.operator, [e.get_ast() for e in self.expressions]


@addToClass(AST.ConstantExpression)
def get_ast(self):
    return str(self.value), []


@addToClass(AST.FunctionExpression)
def get_ast(self):
    return self.name, [a.get_ast() for a in self.arguments]


@addToClass(AST.Identifier)
def get_ast(self):
    return self.name, []


@addToClass(AST.Selector)
def get_ast(self):
    return 'SELECTOR', [self.expression.get_ast(), self.vector.get_ast()]


@addToClass(AST.RangeExpression)
def get_ast(self):
    return 'RANGE', [self.begin.get_ast(), self.end.get_ast()]


@addToClass(AST.VectorExpression)
def get_ast(self):
    return 'VECTOR', [n.get_ast() for n in self.expressions]
