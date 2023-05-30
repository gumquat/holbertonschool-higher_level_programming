#!/usr/bin/python3
"""
5-save_to_json_file
func that writes an obj to a file using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write an obj to txt file using jason
    """
    with open(filename, mode='w', encoding='utf-8') as filefunc:
        json.dump(my_obj, filefunc)
