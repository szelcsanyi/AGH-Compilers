from typing import Any


class Interruption(Exception):
    """ Base exception used for control flow """
    pass


class BreakInterruption(Interruption):
    """ Control flow exception raised in case of break instruction """
    pass


class ContinueInterruption(Interruption):
    """ Control flow exception raised in case of continue instruction """
    pass


class ReturnInterruption(Interruption):
    """ Control flow exception raised is case of return instruction """
    def __init__(self, value: Any):
        self.value = value
