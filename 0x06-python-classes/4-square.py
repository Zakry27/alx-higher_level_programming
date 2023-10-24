#!/usr/bin/python3
"""this defines a square"""


class Square:
    """this defines a square"""
    def __init__(self, size=0):
        """this initialises the data"""
        self.size = size

    def area(self):
        """this returns the current square area"""
        return self.__size**2

    @property
    def size(self):
        """this is the get method"""
        return self.__size

    @size.setter
    def size(self, value):
        """this is the set method"""
        self.__size = value
        if type(value) != int:
            raise TypeError("the size has to be an integer")
        if value < 0:
            raise ValueError("the size has to be >= 0")
