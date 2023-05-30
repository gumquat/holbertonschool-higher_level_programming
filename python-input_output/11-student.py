class Student:
    """
    student class def.
    """
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        func that makes stuff nto jsons
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        makes new instancce with attrs from json
        """
        for key, value in json.items():
            setattr(self, key, value)
