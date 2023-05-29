#!/usr/bin/python3
"""
instantiate with width & height
wdth & height : private and positive integers validated
by integer_validator
print() prints and str() returns specified rectangle
AAAAHHH okay here i go
"""


BaseGeometry = __import__('9-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines Rectangle Class
    """
    def __init__(self, width, height):
        """
        init method
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        returns visually printed rectangle via string e.g. fraction
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Defines square class
    """
    def __init__(self, size):
        """
        init method
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns size
        """
        return (self.__size)
