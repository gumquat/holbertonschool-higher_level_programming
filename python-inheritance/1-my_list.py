#!/usrbin/python3
"""
make a class MyList that inherits from list
"""


class MyList(list):
    """
    print sorted list of self contents
    no change to list
    """
    def print_sorted(self):
            print(sorted(self))
