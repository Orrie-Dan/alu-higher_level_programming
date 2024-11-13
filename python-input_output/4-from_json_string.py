#!/usr/bin/python3
"""
This module provides a function that returns a Python data structure
represented by a given JSON string. The function `from_json_string` converts
a JSON string into the corresponding Python data structure (such as a list,
dictionary, string, etc.).

The function does not import any external modules and manually converts the
JSON string to a Python object.
"""

def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a corresponding Python data structure.

    This function handles various JSON types including strings, numbers,
    booleans, None, lists, and dictionaries, and converts them into their
    equivalent Python representations.

    Args:
        my_str: A JSON string that needs to be converted into a Python object.

    Returns:
        A Python data structure that corresponds to the provided JSON string.

    Raises:
        TypeError: If the JSON string cannot be parsed into a valid Python object.
    """

    # Remove leading and trailing spaces
    my_str = my_str.strip()

    # Handle JSON null (converted to Python None)
    if my_str == "null":
        return None

    # Handle JSON boolean values
    elif my_str == "true":
        return True
    elif my_str == "false":
        return False

    # Handle numbers (integers and floats)
    elif my_str.isdigit() or (my_str[0] == '-' and my_str[1:].isdigit()):  # integer check
        return int(my_str)
    elif my_str.replace('.', '', 1).isdigit() and my_str.count('.') == 1:  # float check
        return float(my_str)

    # Handle strings (must be enclosed in double quotes)
    elif my_str.startswith('"') and my_str.endswith('"'):
        return my_str[1:-1]

    # Handle lists (enclosed in square brackets)
    elif my_str.startswith('[') and my_str.endswith(']'):
        items = my_str[1:-1].strip()  # Remove square brackets
        if not items:
            return []  # Empty list
        # Split items by commas and recursively call `from_json_string` on each item
        return [from_json_string(item.strip()) for item in items.split(',')]

    # Handle dictionaries (enclosed in curly braces)
    elif my_str.startswith('{') and my_str.endswith('}'):
        items = my_str[1:-1].strip()  # Remove curly braces
        if not items:
            return {}  # Empty dictionary
        # Split key-value pairs by commas
        result = {}
        for item in items.split(','):
            key_value = item.split(':', 1)
            if len(key_value) == 2:
                key = from_json_string(key_value[0].strip())
                value = from_json_string(key_value[1].strip())
                result[key] = value
        return result

    # If none of the above conditions match, raise a TypeError
    else:
        raise TypeError("Invalid JSON string")

