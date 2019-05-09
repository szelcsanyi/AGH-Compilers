from functools import singledispatch, update_wrapper

from .SymbolTable import SymbolTable


def method_dispatch(func):
    """
    Decorator that allows for applying functools.singledispatch to methods instead of functions
    Based on: https://stackoverflow.com/a/24602374
    """

    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class CompilerError(Exception):
    def __init__(self, module: str, lineno: int, msg: str, *args: object) -> None:
        super().__init__(msg, *args)
        self.module = module
        self.lineno = lineno
        self.msg = msg

    def __str__(self) -> str:
        return f'{self.module} error (line {self.lineno}): {self.msg}'
