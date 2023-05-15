#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for index in range(len(row) - 1):
            print("{:d}".format(row[index]), end=' ')
        if len(row) > 0:
            print("{:d}".format(row[len(row) - 1]))
        else:
            print()
