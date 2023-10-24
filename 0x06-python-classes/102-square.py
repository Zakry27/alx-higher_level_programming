#!/usr/bin/python3
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
        """this is the getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """this is the setter method"""
        self.__size = value
        if type(value) != int:
            raise TypeError("the size has to be an integer")
        if value < 0:
            raise ValueError("the size has to be >= 0")

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
