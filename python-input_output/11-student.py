#!/usr/bin/python3
"""Student class with JSON serialization and deserialization."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__.copy()
        if not isinstance(attrs, list):
            return self.__dict__.copy()
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
