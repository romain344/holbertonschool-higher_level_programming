#!/usr/bin/python3
"""define la fonction"""


def write_file(filename="", text=""):
    """return aux text written to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
