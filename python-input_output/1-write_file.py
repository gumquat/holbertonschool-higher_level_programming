#!/usr/bin/python3
"""
func that writes text file
"""


def write_file(filename="", text=""):
    """
    write stuff
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        counter = 0
        for element in text:
            counter += 1
        file.write(text)
        return counter
