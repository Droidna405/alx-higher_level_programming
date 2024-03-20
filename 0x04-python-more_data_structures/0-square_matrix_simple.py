#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("Input matrix must be a 2D list with consistent row lengths")
    squared_matrix = [[0 for _ in range(row_length)] for _ in range(len(matrix))]

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            squared_matrix[i][j] = element * element
    return squared_matrix
