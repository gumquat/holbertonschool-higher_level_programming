#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = (0, 0)
    a = 0
    b = 0

    if len(tuple_a) or len(tuple_b) > 0:
        a += tuple_a[0]
        a += tuple_b[0]
        new_tuple = (a, b)
    elif len(tuple_a) or len(tuple_b) > 1:
        b += tuple_a[1]
        b += tuple_b[1]
        new_tuple = (a, b)
    
    return new_tuple