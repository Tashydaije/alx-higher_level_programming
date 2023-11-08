#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix.copy()
    squared_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value**2)
        squared_matrix.append(new_row)
    return squared_matrix
