#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The new matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix does not have the same size.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Validate elements of matrix
    if not all(isinstance(val, (int, float)) for row in matrix
               for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(val / div, 2) for val in row] for row in matrix]
