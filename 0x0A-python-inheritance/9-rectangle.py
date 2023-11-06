#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""the module with the BaseGeometry class"""


class Rectangle(BaseGeometry):
    """BaseGeometry is where the rectangle class comes from."""

    def __init__(self, width, height):
        """the method for initializing the attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method in order to change area method in parent class"""

        return self.__width * self.__height

    def __str__(self):
        """the __str__ method to return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

