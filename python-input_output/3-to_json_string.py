#!/usr/bin/python3
"""
This module provides a function to return the JSON representation of a given object
as a string. The function `to_json_string` handles various Python data types such as
strings, integers, floats, booleans, None, lists, and dictionaries.

The function does not import any external modules and manually converts Python objects
to a JSON-formatted string.
"""

def to_json_string(my_obj):
    """
    Converts a Python object into a JSON-formatted string representation.

    This function handles different Python data types including strings, integers,
    floats, booleans, None, lists, and dictionaries, and converts them into their
    equivalent JSON representation.

    Args:
        my_obj: The Python object to be converted into a JSON string.

    Returns:
        A string representing the JSON-formatted version of the input object.

    Raises:
        TypeError: If the object is of a type that cannot be serialized into JSON.
    """
    if isinstance(my_obj, str):
        return '"' + my_obj + '"'
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif my_obj is None:
        return "null"
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, list):
        return "[" + ", ".join(to_json_string(item) for item in my_obj) + "]"
    elif isinstance(my_obj, dict):
        items = [f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()]
        return "{" + ", ".join(items) + "}"
    else:
        raise TypeError("Object of type '{}' is not serializable".format(type(my_obj).__name__))

