#!/usr/bin/python3


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
        print("#", end="")
        for ii in range(size):
            print("")
