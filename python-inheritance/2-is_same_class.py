#!/usr/bin/python3
"""
function that returns true if the checked object
is 'exactly' an instance of a specified class
otherwise false
"""


def is_same_class(obj, a_class):
    """
    is it an instance of the object?
    """
    return isinstance(obj, a_class)