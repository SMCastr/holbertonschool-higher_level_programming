#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by `div`.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        ValueError: If matrix contains rows of different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], -2)
    [[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]
    >>> matrix_divided([[1.5, 2.8, 3.3], [4.2, 5.5, 6.6]], 2)
    [[0.75, 1.4, 1.65], [2.1, 2.75, 3.3]]
    """
    if not all(isinstance(row, list) for row
            in matrix) or not all(all(isinstance(num, (int, float))
            for num in row) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    def divide_element(num, div):
        return round(num / div, 2)

    new_matrix = [[divide_element(num, div) for num in row] for row in matrix]
    return new_matrix
