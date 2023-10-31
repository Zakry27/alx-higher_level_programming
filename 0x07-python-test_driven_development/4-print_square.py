#!/usr/bin/python3
"""This defines the square printing func"""


def print_square(size):
    """it prints square with # character.

    Args:
        size (int): height/width of square.
    Raises:
        TypeError: If size is not int.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("the size must be an int")
    if size < 0:
        raise ValueError("the size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
