#!/usr/bin/python3
"""the module with the MyList class"""


class MyList(list):
    """the class with the method print_sorted"""
    pass

    def print_sorted(self):
        """the method that sorts a list"""

        print(sorted(list(self)))
