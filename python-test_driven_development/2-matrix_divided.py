#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.

It checks for valid matrix structure and division input,
then returns a new matrix with values rounded to 2 decimals.
"""


def matrix_divided(matrix=None, div=None):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (int or float) not equal to 0, inf, or NaN.

    Returns:
        A new matrix with each value divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if div is not a valid number (or inf/nan),
                   or if matrix rows are uneven.
        ZeroDivisionError: If div is 0.
    """
    if matrix is None or div is None:
        raise TypeError(
            "matrix_divided() missing required arguments "
            + "'matrix' and/or 'div'"
        )

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if matrix == [] or any(row == [] for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if (
        not isinstance(div, (int, float))
        or div != div
        or div == float('inf')
        or div == float('-inf')
    ):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
