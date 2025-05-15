#!/usr/bin/python3
"""
This module provides the function add_integer which adds two numbers.

Examples:
    >>> add_integer(1, 2
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    Traceback (most recent call last):
    TypeError: a must be an integer
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting them to integers).

    Args:
        a: First number (int or float).
        b: Second number (int or float, default is 98).
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)