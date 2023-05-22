#!/usr/bin/python3
# 4-print_square.py
"""square printing function"""


def print_square(size):
    """
    prints a square of specified size

    Args:
        size

    Raises:
        TypeError, ValueError,
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
        for ii in range(size):
            print("")
