#!/usr/bin/python3
"""
This module provides a function to load a Python object from a JSON file.
The function `load_from_json_file` reads the JSON string from a file and
converts it to a Python data structure (such as a dictionary, list, etc.).

No external modules are imported, and the function does not handle exceptions
if the JSON string cannot be parsed or if there are file permission issues.
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

    my_str = my_str.strip()  # Remove leading and trailing spaces

    if my_str == "null":
        return None
    elif my_str == "true":
        return True
    elif my_str == "false":
        return False
    elif my_str.isdigit() or (my_str[0] == '-' and my_str[1:].isdigit()):
        return int(my_str)
    elif my_str.replace('.', '', 1).isdigit() and my_str.count('.') == 1:
        return float(my_str)
    elif my_str.startswith('"') and my_str.endswith('"'):
        return my_str[1:-1]
    elif my_str.startswith('[') and my_str.endswith(']'):
        items = my_str[1:-1].strip()
        if not items:
            return []
        return [from_json_string(item.strip()) for item in items.split(',')]
    elif my_str.startswith('{') and my_str.endswith('}'):
        items = my_str[1:-1].strip()
        if not items:
            return {}
        result = {}
        for item in items.split(','):
            key_value = item.split(':', 1)
            if len(key_value) == 2:
                key = from_json_string(key_value[0].strip())
                value = from_json_string(key_value[1].strip())
                result[key] = value
        return result
    else:
        raise TypeError("Invalid JSON string")

def load_from_json_file(filename):
    """
    Reads a JSON string from a file and converts it to a Python object.

    This function opens the file, reads its contents as a JSON string,
    and then converts that string into the corresponding Python data structure.

    Args:
        filename: The name of the file from which the JSON data will be loaded.

    Returns:
        A Python object (such as a dictionary, list, etc.) corresponding to the
        data in the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_string = file.read()
    return from_json_string(json_string)

