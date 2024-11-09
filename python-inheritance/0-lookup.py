#!/usr/bin/python3
"""
This module defines a function `lookup()` which returns a list of available
attributes and methods of an object. It demonstrates the usage of `dir()`
to inspect objects, and can handle built-in types, user-defined classes,
and instances.

Example Usage:
    - For a built-in type like int, float, or list.
    - For custom user-defined classes and objects.

Each function, class, and test case below is also documented according to
PEP8 style conventions.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to examine.

    Returns:
        list: A list containing the attributes and methods of the object.
    """
    return dir(obj)
