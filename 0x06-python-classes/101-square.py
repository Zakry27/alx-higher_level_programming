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
        """this is the getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """this is the setter method"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("the position has to be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("the position has to be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """this is the same print behaviour as my_print"""
        s = ""
        if not self.__size:
            return s
        for y in range(self.__position[1]):
            s += '\n'
        for i in range(self.__size):
            for x in range(self.__position[0]):
                s += ' '
            for j in range(self.__size):
                s += '#'
            s += '\n'
        return s[: - 1]
