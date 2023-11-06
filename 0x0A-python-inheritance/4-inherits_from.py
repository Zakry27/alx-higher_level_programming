#!/usr/bin/python3
"""the module with the inherits_from method"""


def inherits_from(obj, a_class):
    """method that returns True if object is instance of class that inherited from specified class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
