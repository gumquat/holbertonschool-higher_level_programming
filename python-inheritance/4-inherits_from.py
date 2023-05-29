#!/usr/bin/python3
"""
func that returns True if ...
    obj is instance of a class
    inherited from the
    specified class
    otherwise False.

Prototype -> def inherits_from(obj, a_class):
no modules allowed
"""


def inherits_from(obj, a_class):
    """returns true if obj is instance of parent classes"""
    return isinstance(obj, a_class) and type(obj) is not a_class
