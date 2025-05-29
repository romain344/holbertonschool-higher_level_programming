#!/usr/bin/python3
"""Defines an object attribute lookup function"""
def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False