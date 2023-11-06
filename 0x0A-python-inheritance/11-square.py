#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""the module with the BaseGeometry class"""


class Square(Rectangle):
    """the square class that inherits from Rectangle that inherits from BaseGeometry"""

    def __init__(self, size):
        """the method to initialize the attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """the rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
