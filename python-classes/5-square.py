#!/usr/bin/python3
"""SQUARE STUFF"""


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

    def my_print(self):
        """print the square made of # symbols"""
        if(self.__size <= 0):
            print("")
        else:
            for peepee in range(self.__size):
                for poopoo in range(self.__size):
                    print("#", end='')
            print("")
