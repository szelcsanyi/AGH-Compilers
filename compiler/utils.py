from functools import singledispatch, update_wrapper


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
