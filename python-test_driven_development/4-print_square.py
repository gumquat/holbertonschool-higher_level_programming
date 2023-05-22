#!/usr/bin/python3
#4-print_square
def print_square(size):
    """
    prints a square of specified size

    Args:
        size

    Returns: nothing

    Raises:
        TypeError, ValueError,

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >- 0")

    for i in range (size):
        print("#", end="")
        for ii in range(size):
            print("")
