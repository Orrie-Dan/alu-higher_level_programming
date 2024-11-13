#!/usr/bin/python3

"""
This script adds command-line arguments to a list and saves them to a JSON file.
If the file doesn't exist, it creates the file, and if it exists, it appends
the new arguments to the list stored in the file.
"""

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file, in a format that mimics JSON.
    Args:
        my_obj (list): The list of items to be saved.
        filename (str): The filename to save the list to.
    """
    with open(filename, 'w') as f:
        f.write(str(my_obj).replace("'", '"'))  # Mimicking JSON format


def load_from_json_file(filename):
    """
    Loads a Python object (a list) from a file.
    Args:
        filename (str): The filename from which to load the list.
    Returns:
        list: The list of items, or an empty list if the file doesn't exist.
    """
    try:
        with open(filename, 'r') as f:
            return eval(f.read())  # Convert string back to list
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list


def add_arguments_to_json():
    """
    Adds command-line arguments to a list and saves them to a file.
    """
    import sys  # Import sys to retrieve command-line arguments
    
    # Get the command-line arguments (excluding the script name)
    arguments = sys.argv[1:]

    # Load the existing list from the file (or initialize an empty list if the file doesn't exist)
    existing_data = load_from_json_file('add_item.json')

    # Add the new arguments to the list
    existing_data.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(existing_data, 'add_item.json')


if __name__ == "__main__":
    """
    The entry point for the script.
    It calls the function `add_arguments_to_json()` to load and append arguments to the file.
    """
    add_arguments_to_json()

