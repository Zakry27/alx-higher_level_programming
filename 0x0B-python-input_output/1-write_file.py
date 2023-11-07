#!/usr/bin/python3
"""this defines the file-writing function."""


def write_file(filename="", text=""):
    """Writes string to UTF8 text file.

    Args:
        filename (str): The file's name to be written.
        text (str): text to write to file.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
