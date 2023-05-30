#!/usr/bin/python3
"""
func that reads text file UTF8 and prints STDOUT
"""


def read_file(filename=""):
    """
    print stuff
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
