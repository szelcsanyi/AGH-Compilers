from typing import Any


class Scope(dict):
    """ Scope class which is basically a dict with added name """
    def __init__(self, name: str, *args, **kwargs):
        super(Scope, self).__init__(*args, **kwargs)
        self.name = name


class SymbolTable:

    def __init__(self):
        """ Creates new symbol table with default 'global' scope """
        self.scopes = [Scope('global')]

    def push_scope(self, name: str):
        """ Pushes new scope with given name to scopes stack"""
        self.scopes.append(Scope(name))

    def pop_scope(self):
        """ Pops scope from scopes stack """
        if len(self.scopes) < 2:
            raise ValueError('Cannot pop base scope')
        self.scopes.pop()

    def get_current_scope(self):
        """ Returns current scope, the scope as index -1 """
        return self.scopes[-1]

    def get_parent_scope(self):
        """ Returns parent scope, the scope as index -2 """
        if len(self.scopes) < 2:
            return None
        return self.scopes[-2]

    def get_global_scope(self):
        """ Returns 'global' scope, the scope at index of 0 """
        return self.scopes[0]

    def has_scope(self, name: str):
        """ Checks if there is scope with given name """
        for scope in reversed(self.scopes):
            if scope.name == name:
                return True
        return False

    def __setitem__(self, key: str, value: Any):
        """ Saves symbol in current scope """
        self.get_current_scope()[key] = value

    def __getitem__(self, key):
        """ Returns symbol from symbol table (from current to global scope) """
        for scope in reversed(self.scopes):
            if key in scope:
                return scope[key]
        return None

    def __contains__(self, key):
        """ Checks if given symbol is saved in table """
        for scope in reversed(self.scopes):
            if key in scope:
                return True
        return False
