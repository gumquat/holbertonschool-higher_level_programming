#!/usr/bin/python3
"""
function that returns a list of attributes and 
methods of an object
"""

def lookup(obj):
    """
    lookup - returns a dir() list of the object
    """
    return list(dir(obj))
