#!/usr/bin/python3
"""Script that converts a class instance to a JSON object."""


def class_to_json(obj):

    """Returns the dictionary description with simple data structure"""

    return obj.__dict__
