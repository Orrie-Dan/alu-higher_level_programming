#!/usr/bin/python3

"""
This module defines a function that returns the dictionary description of an object
for JSON serialization. The object is assumed to be an instance of a class, and
all attributes of the class that are serializable (list, dictionary, string, integer,
and boolean) are included in the resulting dictionary.

The function can be used to prepare an object for serialization into formats like
JSON, which requires the object to be represented as a dictionary with serializable values.
"""

def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    The function inspects the attributes of the object (an instance of a class) 
    and creates a dictionary that includes only the attributes that are serializable. 
    The serializable types are: list, dictionary, string, integer, and boolean.

    Args:
        obj (object): The object instance whose attributes will be serialized.

    Returns:
        dict: A dictionary representation of the object's serializable attributes.

    This function excludes any attributes that are not of a serializable type (i.e., 
    other than list, dict, str, int, or bool).

    Example:
        If the object has attributes like `first_name`, `last_name`, `age`, and `courses`,
        and `courses` is a list, the dictionary will include only serializable attributes.
        
        Example:
        >>> student = Student("John", "Doe", 25, ["Math", "Science"])
        >>> class_to_json(student)
        {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'courses': ['Math', 'Science']}
    """
    # Initialize an empty dictionary to hold the serializable attributes
    serializable_dict = {}

    # Iterate over the attributes of the object using its __dict__
    for key, value in vars(obj).items():
        # Check if the value is serializable (i.e., list, dict, str, int, or bool)
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    
    return serializable_dict

