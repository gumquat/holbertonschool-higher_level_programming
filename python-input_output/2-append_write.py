#!/usr/bin/python3
"""
func that appends a string at the end of a file
returns characters added
"""


def append_write(filename="", text=""):
    """
    append file with new line of text
    """

    with open(filename, mode="a", encoding='utf-8') as append:
        counter = 0
        for element in text:
                counter += 1
        append.writelines(text)
        return counter
