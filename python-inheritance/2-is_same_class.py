#!/usr/bin/python3
"""Defines an object attribute lookup function"""
def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False