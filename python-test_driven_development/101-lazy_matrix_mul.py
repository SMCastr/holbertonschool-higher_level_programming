#!/usr/bin/python3
""" 101-lazy_matrix_mul.py"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices, m_a and m_b, using NumPy.
    """
    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except Exception as e:
        raise ValueError("Exception: " + str(e))
