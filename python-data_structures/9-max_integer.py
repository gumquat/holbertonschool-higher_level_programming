#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    else:
        biggest_boy = my_list[0]
        for index in my_list:
            if index > biggest_boy:
                    biggest_boy = index
    return biggest_boy
