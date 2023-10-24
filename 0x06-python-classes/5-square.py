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
        """the getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """the setter method"""
        if type(value) != int:
            raise TypeError("size has to be an integer")
        if value < 0:
            raise ValueError("size has to be >= 0")
        self.__size = value

    def my_print(self):
        """this prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
