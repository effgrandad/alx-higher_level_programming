#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idxx, col in enumerate(new_matrix):
            new_matrix[idx][idxx] = row[idxx] ** 2
    return new_matrix
