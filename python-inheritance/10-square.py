#!/usr/bin/python3
"""defines squares (subclass of rectangles)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines square, subclass of rectangle"""

    def __init__(self, size):
        """init method"""
        self.integer_validator("size", size)
        # super() creates a temporary instance of the obj
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns visually printed rectangle via string e.g. fraction
        """
        return "[Rectangle] {}/{}".format(self.__size)
