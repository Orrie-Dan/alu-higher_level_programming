#!/usr/bin/python3
"""
Module that defines a function to check if an object is exactly an instance of
a specified class.
"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class,
    otherwise returns False.
    
    Parameters:
    obj (any): The object to check.
    a_class (type): The class to compare against.
    
    Returns:
    bool: True if the object is exactly an instance of the specified class, 
          otherwise False.
    """
    return type(obj) is a_class
