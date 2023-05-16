#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    list = set(my_list)
    for num in list:
        sum += num
    return sum
