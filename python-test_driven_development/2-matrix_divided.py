#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.
    
    Args:
        matrix (list of lists): The input matrix of integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if the rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
