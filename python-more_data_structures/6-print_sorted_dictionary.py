#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, element in sorted(a_dictionary.items()):
        print(key, ': ', element, sep='')
    return sorted(a_dictionary.items())
