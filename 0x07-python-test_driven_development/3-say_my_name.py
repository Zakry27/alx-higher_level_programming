#!/usr/bin/python3
"""The function defined here is for printing names."""


def say_my_name(first_name, last_name=""):
    """print the name.

    Args:
        first_name (str): first name to print.
        last_name (str): last name to print.
    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("the first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("the last_name must be string")
    print("My name is {} {}".format(first_name, last_name))
