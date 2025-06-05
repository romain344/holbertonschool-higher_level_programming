#!/usr/bin/python3
"""Write a file with some text and then read it back to verify its contents"""


import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""

    return json.loads(my_str)
