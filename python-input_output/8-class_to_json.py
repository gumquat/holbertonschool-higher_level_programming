#!/usr/bin/python3
"""
8-class_to_json
"""


def class_to_json(obj):
    """
    func that returns dict description of a class
    """
    data = {}

    attributes = vars(obj)

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    
    return data
