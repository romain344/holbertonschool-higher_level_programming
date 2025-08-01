#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """returns the number of characters added to a file."""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
