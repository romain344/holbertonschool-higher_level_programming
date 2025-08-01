#!/usr/bin/python3
"""Script that converts a class instance to a JSON object."""


class Student:
    """define a student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__.copy()
