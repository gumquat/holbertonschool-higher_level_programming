#!/usr/bin/python3
"""
9-student
make a class that defines student by:
first name
last name
age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return 
        {
                attr: getattr(self, attr)
                for attr in attrs
                    if hasattr(self, attr)
            }
