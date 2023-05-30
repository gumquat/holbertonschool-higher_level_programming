#!/usr/bin/python3
"""
6-load_from_json_file
func that creates an obj from a json file
"""
import json


def load_from_json_file(filename):
    """
    func that creates an obj from a json file
    """
    with open(filename, mode='r', encoding='utf-8') as filefunc:
        data = json.load(filefunc)
    return data
