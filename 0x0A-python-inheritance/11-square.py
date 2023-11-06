#!/usr/bin/python3
"""Define Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """Initializes new square.

        Args:
            size (int): size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
