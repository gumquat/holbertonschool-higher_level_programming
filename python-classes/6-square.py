#!/usr/bin/python3
"""WHY IS MY OUTPUT INCORRECT IF I DONT HAVE THE () ON THE LINE BELOW???"""


class Square():
    """this class defines squares"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """calc & return area"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if(self.__size <= 0):
            print()
        else:
            for peepee in range(self.position[1]):
                print()
            for peepee in range(self.size):
                for poopoo in range(self.position[0]):
                    print(end=" ")
                for peepeepoopoo in range(self.size):
                    print("#", end="")
                print()
