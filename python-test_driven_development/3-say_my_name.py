#!/usr/bin/python3
"""
This module contains a function `say_my_name` that prints the full name 
using the provided first name and last name. The function checks that 
both arguments are strings, otherwise raises a TypeError.
"""

def say_my_name(first_name, last_name=""):
    """Prints the full name in the format: My name is <first_name> <last_name>"""
    
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted name
    print(f"My name is {first_name} {last_name}")

