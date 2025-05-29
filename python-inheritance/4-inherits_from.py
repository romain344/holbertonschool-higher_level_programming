#!/usr/bin/python3
"""Defines an object attribute inherits_from function"""
def inherits_from(obj, a_class):
    """define the function inherits_from"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False