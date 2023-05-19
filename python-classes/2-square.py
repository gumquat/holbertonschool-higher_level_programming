#!/usr/bin/python3
"""class for squares (haha thats you):"""


class Square:
    """this class defines squares with size"""
    def __init__(self, size=0):
        self._size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
