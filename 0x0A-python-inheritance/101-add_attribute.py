#!/usr/bin/python3
"""this defines func that adds attributes to objects."""


def add_attribute(obj, att, value):
    """it adds new attribute to object if possible."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
