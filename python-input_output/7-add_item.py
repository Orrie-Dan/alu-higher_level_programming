#!/usr/bin/python3

"""
This module allows you to add command-line arguments to a list and save them to a file.
If the file doesn't exist, it is created, and if it exists, the arguments are appended.
"""

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object (a list) to a file in a JSON-like format.
    
    Args:
        my_obj (list): The Python list to save to the file.
        filename (str): The file to save the list to.
    """
    with open(filename, 'w') as f:
        # Write the list to the file, using double quotes for JSON-like formatting
        f.write(str(my_obj).replace("'", '"'))  # Mimicking JSON format


def load_from_json_file(filename):
    """
    Loads a Python object (a list) from a file in a JSON-like format.
    
    Args:
        filename (str): The file to load the list from.
    
    Returns:
        list: The list from the file, or an empty list if the file doesn't exist.
    """
    try:
        with open(filename, 'r') as f:
            # Read the content of the file and convert it back to a list using eval()
            return eval(f.read())  # Convert string back to a list (JSON-like)
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list


def add_arguments_to_json():
    """
    Adds command-line arguments to a list and saves them to a file.
    
    The arguments passed to the script are loaded into a list, and the list is saved to
    the 'add_item.json' file. If the file does not exist, it is created.
    """
    import sys  # Import sys to retrieve the command-line arguments
    
    # Retrieve the arguments passed to the script, excluding the script name
    arguments = sys.argv[1:]

    # Load the existing data from 'add_item.json' (or initialize an empty list if it doesn't exist)
    existing_data = load_from_json_file('add_item.json')

    # Append the new arguments to the existing data
    existing_data.extend(arguments)

    # Save the updated list back to 'add_item.json'
    save_to_json_file(existing_data, 'add_item.json')


if __name__ == "__main__":
    """
    Main entry point for the script.
    It will call `add_arguments_to_json()` to load and append arguments to the file.
    """
    add_arguments_to_json()

