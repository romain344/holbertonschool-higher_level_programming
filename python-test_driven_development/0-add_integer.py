#!/usr/bin/python3
""" Module 0-add_integer: adds two integers """

def add_integer(a, b=98):
    """
    Adds two integers a and b.

    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Returns:
        int: sum of a and b as integers

    Raises:
        TypeError: if a or b are not integers or floats

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
