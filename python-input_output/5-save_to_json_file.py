#!/usr/bin/python3
"""
This module provides a function to write a Python object to a text file in its
JSON representation. The function `save_to_json_file` takes an object and a
filename as input, converts the object to a JSON-formatted string, and writes
the string to the specified file.

No external modules are imported, and the function does not handle exceptions
if the object cannot be serialized or if there are file permission issues.
"""

def to_json_string(my_obj):
    """
    Converts a Python object into a JSON-formatted string representation.

    This function handles different Python data types including strings, integers,
    floats, booleans, None, lists, and dictionaries, and converts them into their
    equivalent JSON representations.

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


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file as its JSON representation.

    This function converts the given Python object to a JSON string and writes
    that string to a file specified by the `filename` argument. The function
    uses the `with` statement to open and close the file.

    Args:
        my_obj: The Python object to be written to the file.
        filename: The name of the file where the JSON representation will be saved.
    """
    json_string = to_json_string(my_obj)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_string)

