#!/usr/bin/python3

"""
This module contains a function add_integer which adds two integers or floats.
If either input is a float, it is cast to an integer before the addition.
The function raises a TypeError if either argument is not an integer or a float.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats. If either input is a float, it will be cast to an integer.
    If the inputs are not integers or floats, a TypeError is raised.

    Args:
        a: First number, can be an integer or a float.
        b: Second number, can be an integer or a float (default is 98).

    Returns:
        int: The sum of the two numbers as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b

