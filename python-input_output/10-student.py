#!/usr/bin/python3
""" """


class Student:
    """define a student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            return self
        if not isinstance(attrs, list):
            return self