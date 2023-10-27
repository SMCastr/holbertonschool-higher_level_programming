#!/usr/bin/python3
"""101-lazy_matrix_mul.py  """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a and m_b can't be empty")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must have the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("ma and mb can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
