#!/usr/bin/python3
"""this defines the string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of string object."""
    return json.dumps(my_obj)
