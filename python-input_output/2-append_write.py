#!/usr/bin/python3
"""define la finctiont"""
def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added"""

    with open(filename, 'a', encoding='utf8') as filename:
        return filename.write(text)