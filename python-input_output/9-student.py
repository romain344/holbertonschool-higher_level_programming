#!/usr/bin/python3
"""Script that converts a class instance to a JSON object."""


class Student:
    """define a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return self.__dict__
