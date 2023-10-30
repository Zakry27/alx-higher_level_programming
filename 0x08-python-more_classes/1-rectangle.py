#!/usr/bin/python3
"""The Rectangle class is defined by this."""


class Rectangle:
    """this represents the rectangle."""

    def __init__(self, width=0, height=0):
        """this initializes the new Rectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the width must be an int")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the height must be an int")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value
