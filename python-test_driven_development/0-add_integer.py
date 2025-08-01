#!/usr/bin/python3
"""défine la fonction"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to integers).
    
    Args:
        a: First number (integer or float)
        b: Second number (integer or float, defaults to 98)
        
    Returns:
        int: Sum of a and b after casting to integers
        
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)
