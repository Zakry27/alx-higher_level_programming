#!/usr/bin/python3
"""this defines the JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns Python object representation of JSON string."""
    return json.loads(my_str)
