#!/usr/bin/python3
"""
0-add_integer.py
prints the sum of two arguments if they are ints/floats
"""


def add_integers(a, b=98):
    """
    Return sum of arguments

    check if data passed are both type int

    arguments are typcasted as ints for the return

    Raises: TypeError: If either argument is not type int/float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
