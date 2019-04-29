""" Module implementing visitor pattern """

from collections import defaultdict
from typing import Type


def _not_implemented(obj):
    raise NotImplemented(f'No handler provided for type {type(obj)}')


class Visitor:

    def __init__(self):
        """ Creates visitor """
        self._default_handler = _not_implemented
        self._handlers = defaultdict(lambda obj: self._default_handler)

    def default(self, f):
        """
        Decorator that registers decorated function as default handler
        :param f: default handler
        :return:
        """
        self._default_handler = f
        return f

    def handler(self, arg_type: Type[object]):
        """
        Decorator that registers decorated function to be used for given type
        :param arg_type: type that will be associated with decorated function
        :return: decorator
        """

        def handler_decorator(f):
            self._handlers[arg_type] = f
            return f

        return handler_decorator

    def visit(self, obj):
        """ Visits given object """
        self._handlers[type(obj)](obj)
