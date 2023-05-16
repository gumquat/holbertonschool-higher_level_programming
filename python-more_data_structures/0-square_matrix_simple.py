#!/usr/bin/python3
def squaring (num):
    return num ** num

def square_matrix_simple(matrix=[]):

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in matrix[i]:
            new_matrix[i].append([])

    return(map(squaring, new_matrix))
