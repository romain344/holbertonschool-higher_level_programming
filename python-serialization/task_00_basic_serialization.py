#!/usr/bin/python3
"""initialize le code"""


import json

def serialize_and_save_to_file(data, filename):
    """define la function """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        return json.load(f)
