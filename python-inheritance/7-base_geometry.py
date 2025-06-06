#!/usr/bin/python3
"""BaseGeometry class definition."""


class BaseGeometry:
    """BaseGeometry class with public"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
