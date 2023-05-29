#!/usr/bin/python3
"""
func that returns true if is an instance
or if object is an instace of the class its inherited from
otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if obj is instance of class
    """
    return isinstance(obj, a_class)
