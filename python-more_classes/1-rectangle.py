#!/usr/bin/python3
# 0-rectangle.py
"""
empty class defining rectangles
"""


class Rectangle:
    """
    this defines rectangles
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

"""
PROPERTIES
"""
@property
def width(self):
    return self.__width

@property
def height(self):
    return self.__height

"""
SETTERS
"""
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
    elif value > 0:
        raise TypeError("height must be >= 0")
    else:
        self.__height = value
