#!/usr/bin/python3
"""the module with the is_same_class method"""


def is_same_class(obj, a_class):
    """the method that returns True if object is the instance of class"""

    return type(obj) is a_class
