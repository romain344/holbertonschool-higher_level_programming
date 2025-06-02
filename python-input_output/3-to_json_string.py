#!/usr/bin/python3
"""definies a function that writes a string to a text file"""


import json
def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""

    return json.dumps(my_obj)
