#!/usr/bin/python3
"""this defines the Python class-to-JSON function."""


def class_to_json(obj):
    """Provides dictionary representation for simple data structure."""
    return obj.__dict__
