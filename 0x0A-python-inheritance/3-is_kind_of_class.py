#!/usr/bin/python3
"""the module with the is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from"""

    return isinstance(obj, a_class)
