#!/usr/bin/python3
"""the module with the BaseGeometry class"""


class BaseGeometry:
    """the BaseGeometry class"""

    def area(self):
        """the method for the calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for validating if num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an int".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
