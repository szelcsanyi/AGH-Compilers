from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type, Tuple, ClassVar


@dataclass(frozen=True)
class MType:
    type: Optional[Type]
    shape: Tuple[Optional[int], ...] = tuple()

    def is_scalar(self):
        return len(self.shape) < 1

    def is_vector(self):
        return len(self.shape) == 1

    def is_matrix(self):
        return len(self.shape) > 1

    def __repr__(self):
        repr = self.type.__name__ if self.type else 'None'
        if not self.is_scalar():
            shape = ['*' if d is None else str(d) for d in iter(self.shape)]
            repr += '[' + ','.join(shape) + ']'
        return repr

    # class constants
    NONE: ClassVar[MType]
    BOOL: ClassVar[MType]
    STR: ClassVar[MType]
    INT: ClassVar[MType]
    FLOAT: ClassVar[MType]
    EMPTY_VECTOR: ClassVar[MType]


# initialize class constants
MType.NONE = MType(None)
MType.BOOL = MType(bool)
MType.STR = MType(str)
MType.INT = MType(int)
MType.FLOAT = MType(float)
MType.EMPTY_VECTOR = MType(None, (0, ))
