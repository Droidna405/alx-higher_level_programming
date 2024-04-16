#!/usr/bin/python3
"""pascal's triangle to the nth row"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """

    if n <= 0:
        return []
    # Initialize an empty list to store the triangle
    triangle = []

    # Loop through each row
    for i in range(n):
        # Create a new row list
        row = []
        # Loop through each element in the row
        for j in range(i + 1):
            # If it's the first or last element in the row, it's always 1
            if j == 0 or j == i:
                row.append(1)

        else:
            if i - 1 >= 0:
                left_val = triangle[i - 1][j - 1] if j - 1 >= 0 else 0
                right_val = triangle[i - 1][j] if j < len(
                    triangle[i - 1]) else 0
                row.append(left_val + right_val)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
        triangle (list): A list of lists representing Pascal's triangle.

    Returns:
        None

    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
