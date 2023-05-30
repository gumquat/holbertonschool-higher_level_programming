#!/usr/bin/python3
"""
func that writes text file
"""


def write_file(filename="", text=""):
    """
    write stuff
    """
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
