#!/usr/bin/python3
def element_at(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[idx]
    else:
        my_list[idx] = element
