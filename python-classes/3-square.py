#!/usr/bin/python3
"""SQUARES"""


class Square:
    """this class defines squares"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """calc & return area"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value