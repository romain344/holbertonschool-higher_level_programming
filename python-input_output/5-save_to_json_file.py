#!/usr/bin/python3
"""Write a Python object to a text file using JSON representation"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(my_obj, f)
