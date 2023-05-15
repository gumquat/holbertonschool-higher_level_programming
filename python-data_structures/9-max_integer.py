#!/usr/bin/python3
def max_integer(my_list=[]):

    if ((len(my_list)) == 0):
        return (None)
    else:
        for index in my_list:
            biggest_boy = my_list[0]
            if (biggest_boy < index):
                    biggest_boy = index
            return biggest_boy
