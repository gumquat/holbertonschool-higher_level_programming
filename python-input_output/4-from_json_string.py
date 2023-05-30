#!/usr/bin/python3
"""
func that returns an obj represented by json string
"""


import json


def from_json_string(my_str):
    """
    from json to string converter
    """
    return json.loads(my_str)
