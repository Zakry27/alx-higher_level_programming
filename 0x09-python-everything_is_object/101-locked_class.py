#!/usr/bin/python3
"""Sets forth a class that is locked"""


class LockedClass:
    """
    this prevents user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
