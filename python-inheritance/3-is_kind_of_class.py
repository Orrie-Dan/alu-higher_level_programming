#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of a class 
or any of its subclasses.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class. Otherwise, returns False.
    
    Parameters:
    obj (any): The object to check.
    a_class (type): The class to compare against.
    
    Returns:
    bool: True if the object is an instance of the specified class or a subclass,
          otherwise False.
    """
    return isinstance(obj, a_class)
