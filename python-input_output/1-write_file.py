#!/usr/bin/python3
"""definie"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written"""

    with open(filename, 'r', encoding='utf8') as filename:
        return filename.write(text)
