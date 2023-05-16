#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix=[]
    
    for idx1 in range (len(matrix)):
        new_matrix.append([])
        for idx2 in matrix[idx1]:
            new_matrix[idx1].append(idx2 ** idx2)
    return new_matrix