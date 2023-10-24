#!/usr/bin/python3
class Square:
    """this defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """this initialises the data"""
        self.size = size
        self.position = position

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
        self.__size = value
        if type(value) != int:
            raise TypeError("size has to be an integer")
        if value < 0:
            raise ValueError("size has to be >= 0")

    def my_print(self):
        """this prints the square"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """the getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """the setter method"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("the position must be the tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("the position must be the tuple of 2 positive integers")
        self.__position = value