#!/usr/bin/python3
"""define"""


def read_file(filename=""):
    """definie la fonction"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
