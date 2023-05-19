#!/usr/bin/python3
"""an empty class for squares:"""


class Square:
    """this class defines squares"""
    def __init__(self, size=0):
        """this initializes sqaures"""
        if type(size) is not int:
            raise TypeError("size can't be an integer")
        if size < 0:
            raise ValueError("size can't be =< 0")
        self._size = size
