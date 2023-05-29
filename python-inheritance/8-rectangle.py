#!/usr/bin/python3
"""
class that inherits from BaseGeometry-7
instantiate width and height
width and height are private
width and height must be positive ints, validated by integer_validator
AAAAHHH okay here i go
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
