import operator

import numpy as np

OPERATORS = {
    '+':        operator.add,
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
    'eye':      np.eye,
    'zeros':    np.zeros,
    'ones':     np.ones
}
