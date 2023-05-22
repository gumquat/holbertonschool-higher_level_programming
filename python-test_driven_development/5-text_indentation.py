#!/usr/bin/python3
# 5-text-indentation.py
"""indents text given"""


def text_indentation(text):
    """
    prints text with new lines when . ? and :

    Args: 
        text

    Raises:
        TypeError
    """

    characters = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')
        if char in characters:
            print()
            print()
