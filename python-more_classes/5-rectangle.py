#!/usr/bin/python3
# 1-rectangle.py
"""
CLASS defining rectangles
"""


class Rectangle:
    """
    this defines rectangles
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return ((self.width * 2) + (self.height * 2))
        else:
            return 0

    def __str__(self):
        if self.width > 0 and self.height > 0:
            return '\n'.join(['#' * self.width for _ in range(self.height)])
        else:
            return ''

    def __repr__(self):
        """
        returns a literal string with quotes for humans
        """
        return ("Rectangle ({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
