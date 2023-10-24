#!/usr/bin/python3
class Square:
    """this defines a square"""
    def __init__(self, size=0):
        """this initialises the data"""
        self.__size = size
        if type(size) != int:
            raise TypeError("the size has to be an integer")
        if size < 0:
            raise ValueError("the size has to be >= 0")

    def area(self):
        """this returns the current square area"""
        return self.__size**2
