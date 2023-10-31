#!/usr/bin/python3
"""NumPy is used to define the matrix multiply function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this return multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
