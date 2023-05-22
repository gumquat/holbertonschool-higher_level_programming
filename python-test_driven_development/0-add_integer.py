#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Return sum of the arguments

    floats are typcasted to ints for good accpetable value

    Raises:
        TypeError: either a/b is a non-int/float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)