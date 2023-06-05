#!/usr/bin/python3
"""BASE. BASE. BASE."""
import json


class Base:
    """base class for further geometry"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """
    STATIC METHODS
    --------------
    """

    @staticmethod
    def to_json_string(list_dictionaries):
        """func makes json files"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return: list of json string data"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    """
    CLASS METHODS
    -------------
    """

    @classmethod
    def save_to_file(cls, list_objs):
        """func writes json str to a file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """return: instance w attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return: list of instances"""
        the_file = cls.__name__ + ".json"
        all_instances = []
        try:
            with open(the_file, 'r', encoding='utf-8') as file:
                all_instances = cls.from_json_string(file.read())
            for key, value in enumerate(all_instances):
                all_instances[key] = cls.create(**all_instances[key])
        except:
            pass
        return all_instances
