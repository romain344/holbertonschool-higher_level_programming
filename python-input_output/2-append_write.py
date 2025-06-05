#!/usr/bin/python3
"""Module that defines a function to append text to a file."""

def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added"""

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)