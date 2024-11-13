#!/usr/bin/python3

"""
This script adds all arguments passed from the command line to a Python list
and saves the updated list to a JSON file named 'add_item.json'. If the file 
doesn't exist, it is created. If the file already exists, the new arguments 
are appended to the existing list.

The script doesn't use any external modules; everything is done manually.
"""

def to_json_string(my_obj):
    """
    Converts a Python object (list, dictionary, etc.) to a JSON-formatted string.
    
    Args:
        my_obj: The Python object to be converted into a JSON string.

    Returns:
        A JSON string representing the Python object.
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
        raise TypeError(f"Object of type '{type(my_obj).__name__}' is not serializable")

def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object (list, dictionary, etc.).

    Args:
        my_str: The JSON string to be converted into a Python object.

    Returns:
        The corresponding Python object (list, dictionary, etc.).
    """
    my_str = my_str.strip()  # Strip leading/trailing spaces

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
        return my_str[1:-1]  # Strip quotes for string
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

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a JSON file.

    Args:
        my_obj: The Python object to be written to the file.
        filename: The name of the file to which the JSON string will be saved.
    """
    json_string = to_json_string(my_obj)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_string)

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename: The name of the file from which the JSON data will be loaded.

    Returns:
        A Python object (list, dictionary, etc.) corresponding to the data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_string = file.read()
    return from_json_string(json_string)

def main():
    """
    Main function that handles command-line arguments, loads the existing 
    list from 'add_item.json', appends the new arguments, and saves the updated 
    list back to the file.
    """
    # Get the arguments from command line, excluding the script name
    arguments = sys.argv[1:]

    # Try to load the existing list from the file
    try:
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        current_list = []

    # Add the new arguments to the list
    current_list.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(current_list, "add_item.json")

if __name__ == "__main__":
    """
    Entry point of the script. When the script is executed, it calls the main 
    function to process the command-line arguments and update the JSON file.
    """
    main()

