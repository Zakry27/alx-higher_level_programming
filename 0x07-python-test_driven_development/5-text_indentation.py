#!/usr/bin/python3
"""the text-indentation func."""


def text_indentation(text):
    """Produce the text with two new lines following every . '.', '?', and ':'.

    Args:
        text (string): text to print.
    Raises:
        TypeError: If text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("the text must be string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
