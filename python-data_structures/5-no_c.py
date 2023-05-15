#!/usr/bin/python3
def no_c(my_string):
    buffer_string = ""
    if my_string:
        for char in my_string:
            if char != "c" and char != "C":
                buffer_string += char
    return buffer_string
