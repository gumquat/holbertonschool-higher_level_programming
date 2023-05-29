#!/usr/bin/python3
"""
func that returns true is obj is an instance of a class
that inherited from the specified class

otherwise false

prototype: def inherits_from()
"""


def inherits_From(obj, a_class):
    """
    returns true if obj is instance of parent class

    otherwise false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
