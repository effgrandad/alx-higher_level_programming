#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    
    new_matrix = matrix.copy()
    for h in range(len(matrix)):
        new_matrix[x] = list(map(lambda x: x**2, matrix[h]))
    return (new_matrix)
