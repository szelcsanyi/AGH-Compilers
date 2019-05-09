import operator
from typing import Type, Any, Callable, Dict

import numpy as np

from compiler.interpreter.interuptions import BreakInterruption, ContinueInterruption, ReturnInterruption


def raise_operation(err: Type[Exception]) -> Callable:
    """ Returns function that raises given exception """
    def func(*args):
        raise err(*args)
    return func


def extended_add(a: Any, b: Any) -> Any:
    """ Add operation extended with str support """
    if a is str or b is str:
        a = str(a)
        b = str(b)
    return a + b


def parse_tuple(f: Callable) -> Callable:
    """ Decorates given function by casting arguments to one tuple """
    def func(*args):
        return f(tuple(args))
    return func


OPERATIONS: Dict[str, Callable] = {
    'u-':       operator.neg,
    '+':        extended_add,
    '-':        operator.sub,
    '*':        operator.mul,
    '/':        operator.truediv,
    '==':       operator.eq,
    '!=':       operator.ne,
    '>':        operator.gt,
    '<':        operator.lt,
    '>=':       operator.ge,
    '<=':       operator.le,
    '.+':       np.add,
    '.-':       np.subtract,
    '.*':       np.multiply,
    './':       np.divide,
    '\'':       np.transpose,
    'eye':      np.eye,
    'zeros':    parse_tuple(np.zeros),
    'ones':     parse_tuple(np.ones),
    'break':    raise_operation(BreakInterruption),
    'continue': raise_operation(ContinueInterruption),
    'return':   raise_operation(ReturnInterruption),
    'print':    print
}
