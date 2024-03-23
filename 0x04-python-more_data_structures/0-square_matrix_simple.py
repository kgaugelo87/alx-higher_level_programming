#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_sq_matrix = []
    for i in matrix:
        new_sq_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return new_sq_matrix
