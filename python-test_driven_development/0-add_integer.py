#!/usr/bin/python3
def add_integers(a, b=98):
    """check if data passed are both type int"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (a + b)
