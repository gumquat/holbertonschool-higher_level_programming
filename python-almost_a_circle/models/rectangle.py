#!/usr/bin/python3
"""rectangle class"""


from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validate and set width"""
        #__
        self.width = self.HW_validator("width", value)

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validate and set height"""
        #__
        self.height = self.HW_validator("height", value)

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """validate and set x"""
        #__
        self.x = self.XY_validator("x", value)

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """validate and set y"""
        #__
        self.y = self.XY_validator("y", value)

    def area(self):
        """init area"""
        #__
        return self.width * self.height

    def display(self):
        """prints out a string representation of the rectangle"""
        for i in range(self.y):
            print()
        for a in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """func overwrites __str___ of base"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns args to attributes"""
        if args:
            atts = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, atts[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    """HEIGHT & WIDTH VALIDATOR"""
    def HW_validator(self, name, value):
        """
        Raises Errors if...
        1.) TypeError if Value =/= int
        2.) ValueError if Value <=0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be > 0".format(name))
        return (value)

    """X & Y VALIDATOR"""
    def XY_validator(self, name, value):
        """
        Raises Errors if...
        1.) TypeError if Value =/= int
        2.) ValueError if Value <=0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be >= 0".format(name))
        if value > 0:
            raise ValueError("{} must be >= 0".format(name))
        return (value)
