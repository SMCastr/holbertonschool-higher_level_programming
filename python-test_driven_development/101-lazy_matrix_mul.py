#!/usr/bin/python3
"""101-lazy_matrix_mul.py"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("Incompatible matrices for multiplication")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
