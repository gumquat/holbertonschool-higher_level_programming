#!/usr/bin/python3
"""square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format\
            (self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """init size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """self updating"""
        attrs, i = ['id', 'size', 'x', 'y'], 0
        if args:
            for value in args:
                setattr(self, attrs[i], value)
                i += 1
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns rectangle def"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
