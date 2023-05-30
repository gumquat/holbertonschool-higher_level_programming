#!/usr/bin/python3
"""
func that writes text file
"""


def write_file(filename="", text=""):
    """
    write stuff
    """
    with open(filename, "w", encoding="utf-8") as file:
        counter += 1
        # return file.write(text)
        return counter
