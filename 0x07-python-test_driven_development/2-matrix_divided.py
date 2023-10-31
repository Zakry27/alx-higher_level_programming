#!/usr/bin/python3
"""this defines the matrix division func"""


def matrix_divided(matrix, div):
    """this divides all elements of the matrix.

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): divisor.
    Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        new matrix representing result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix must have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("the div must be number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
