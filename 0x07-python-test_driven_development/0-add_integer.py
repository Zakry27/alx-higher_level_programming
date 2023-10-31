#!/usr/bin/python3
"""Creates a function that adds integers."""


def add_integer(a, b=98):
    """this returns the int addition of a and b.

    Typecasting float arguments to integers is done before adding them.

    Raises:
        TypeError: If a or b is non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an int")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an int")
    return (int(a) + int(b))
