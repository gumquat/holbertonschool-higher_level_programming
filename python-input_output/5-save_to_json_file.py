#!/usr/bin/python3
"""
5-save_to_jason_file
func that writes an obj to a text file using json represenstation
Prototype: ...
Def: ...
Return: ...
"""
import json


def save_to_jason_file(my_obj, filename):
    """here go dat boi oml he schmovin"""
    with open(filename, mode="w", encoding="utf-8") as filefunc:
        json.dump(my_obj, filefunc)
