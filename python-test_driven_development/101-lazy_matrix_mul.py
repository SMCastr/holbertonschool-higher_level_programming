#!/usr/bin/env python3
""" Module for lazy_matrix_mul method"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()  # Convert the NumPy array back to a list of lists
    except ValueError as e:
        raise ValueError("Incompatible matrices for multiplication") from e
