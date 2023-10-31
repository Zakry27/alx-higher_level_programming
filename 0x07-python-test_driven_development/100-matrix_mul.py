#!/usr/bin/python3
"""matrix multiply func"""


def matrix_mul(m_a, m_b):
    """it multiplies two matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    Raises:
        TypeError: If m_a or m_b aren't list of lists of ints/floats.
        TypeError: If m_a or m_b are empty.
        TypeError: If m_a or m_b have different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        new matrix representing multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a cannot be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b cannot be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only ints or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only ints or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
