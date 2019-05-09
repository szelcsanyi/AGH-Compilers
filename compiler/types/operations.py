from compiler.types import MType

UNARY_MINUS = {
    MType.BOOL:   MType.INT,
    MType.INT:    MType.INT,
    MType.FLOAT:  MType.FLOAT
}

PLUS = {
    (MType.BOOL,    MType.BOOL):    MType.INT,
    (MType.BOOL,    MType.STR):     MType.STR,
    (MType.BOOL,    MType.INT):     MType.INT,
    (MType.BOOL,    MType.FLOAT):   MType.FLOAT,

    (MType.STR,     MType.BOOL):    MType.STR,
    (MType.STR,     MType.STR):     MType.STR,
    (MType.STR,     MType.INT):     MType.STR,
    (MType.STR,     MType.FLOAT):   MType.STR,

    (MType.INT,     MType.BOOL):    MType.INT,
    (MType.INT,     MType.STR):     MType.STR,
    (MType.INT,     MType.INT):     MType.INT,
    (MType.INT,     MType.FLOAT):   MType.FLOAT,

    (MType.FLOAT,   MType.BOOL):    MType.FLOAT,
    (MType.FLOAT,   MType.STR):     MType.STR,
    (MType.FLOAT,   MType.INT):     MType.FLOAT,
    (MType.FLOAT,   MType.FLOAT):   MType.FLOAT,
}

MINUS = TIMES = DIVIDE = {
    (MType.BOOL,    MType.BOOL):    MType.INT,
    (MType.BOOL,    MType.INT):     MType.INT,
    (MType.BOOL,    MType.FLOAT):   MType.FLOAT,

    (MType.INT,     MType.BOOL):    MType.INT,
    (MType.INT,     MType.INT):     MType.INT,
    (MType.INT,     MType.FLOAT):   MType.FLOAT,

    (MType.FLOAT,   MType.BOOL):    MType.FLOAT,
    (MType.FLOAT,   MType.INT):     MType.FLOAT,
    (MType.FLOAT,   MType.FLOAT):   MType.FLOAT,
}

GREATER = LESSER = GREATER_OR_EQUAL = LESSER_OR_EQUAL = {
    (MType.BOOL,    MType.BOOL):    MType.BOOL,
    (MType.BOOL,    MType.INT):     MType.BOOL,
    (MType.BOOL,    MType.FLOAT):   MType.BOOL,

    (MType.INT,     MType.BOOL):    MType.BOOL,
    (MType.INT,     MType.INT):     MType.BOOL,
    (MType.INT,     MType.FLOAT):   MType.BOOL,

    (MType.FLOAT,   MType.BOOL):    MType.BOOL,
    (MType.FLOAT,   MType.INT):     MType.BOOL,
    (MType.FLOAT,   MType.FLOAT):   MType.BOOL,
}

SCALAR_OPERATORS = {
    '+': PLUS,
    '-': MINUS,
    '*': TIMES,
    '/': DIVIDE,
    '>': GREATER,
    '<': LESSER,
    '>=': GREATER_OR_EQUAL,
    '<=': LESSER_OR_EQUAL
}
