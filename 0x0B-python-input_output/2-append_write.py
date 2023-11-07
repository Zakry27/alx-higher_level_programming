#!/usr/bin/python3
"""this defines the file-appending function."""


def append_write(filename="", text=""):
    """The end of the UTF8 text file is populated with a string.

    Args:
        filename (str): name of file to append to.
        text (str): string to append to file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
