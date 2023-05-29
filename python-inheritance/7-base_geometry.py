#!/usr/bin/python3
""" empty class called BasseGeometry"""


class BaseGeometry:
    "class defines BaseGeometry"
    def area(self):
        """Public Instance Method: Area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Public Instance Method: Integer Validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
