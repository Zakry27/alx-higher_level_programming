#!/usr/bin/python3
"""this define MagicClass matching exactly a bytecode provided by ALX."""

import math


class MagicClass:
    """this represent a circle."""

    def __init__(self, radius=0):
        """this initialize a MagicClass.

        Arg:
            radius (float or int): radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """this return the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """this return The circumference of MagicClass."""
        return (2 * math.pi * self.__radius)
