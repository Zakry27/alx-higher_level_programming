#!/usr/bin/python3
"""this Defines base geometry class BaseGeometry."""


class BaseGeometry:
    """this represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate a parameter as int.

        Args:
            name (str): name of parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be int".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
