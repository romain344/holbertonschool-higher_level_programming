#!/usr/bin/python3
"""Write a file with some text and then read it back to verify its contents"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""

    with open(filename, 'r', encoding='utf8') as filename:
        return json.load(filename)
