#!/usr/bin/python3
"""
func that writes an pbj to a text file using json represenstation
"""
import json


def save_to_jason_file(my_obj, filename):
    """
    here go dat boi oml he schmovin
    here go dat boi oml he schmovin
    """
    with open(filename, mode="w", encoding="json") as booger:
        json.dump(my_obj, booger)
