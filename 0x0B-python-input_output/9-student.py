#!/usr/bin/python3
"""this defines the class Student."""


class Student:
    """this represents student."""

    def __init__(self, first_name, last_name, age):
        """this initializes new Student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this gets dictionary representation of Student."""
        return self.__dict__
