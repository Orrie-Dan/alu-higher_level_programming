#!/usr/bin/python3

"""
This module provides functionality to:
1. Collect command-line arguments passed to the script.
2. Load a list from a JSON-like file ('add_item.json') if it exists.
3. Append the new arguments to the existing list.
4. Save the updated list back to the JSON-like file.

The script assumes that the file may or may not exist and will create the file if necessary.
"""

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object (in this case, a list) to a file in a simple JSON-like format.

    This function converts the list to a string, replacing single quotes with double quotes
    to mimic a JSON format, and writes it to a file. If the file exists, it will be overwritten.
    
    Args:
        my_obj (list): The Python list to save to the file.
        filename (str): The name of the file to write the list to.
        
    Example:
        save_to_json_file([1, 2, 3], "add_item.json")
        # This will save the list [1, 2, 3] to the file 'add_item.json' in JSON-like format.
    """
    with open(filename, 'w') as f:
        # Convert the list to a string and replace single quotes with double quotes
        f.write(str(my_obj).replace("'", '"'))  # Mimics JSON formatting


def load_from_json_file(filename):
    """
    Loads a Python object (list) from a JSON-like file.

    This function reads a file and converts the string representation of a list back to a
    Python list using `eval()`. If the file does not exist, an empty list is returned.
    
    Args:
        filename (str): The name of the file to load the list from.
        
    Returns:
        list: The list from the file, or an empty list if the file doesn't exist.
        
    Example:
        load_from_json_file("add_item.json")
        # If the file contains '["apple", "banana"]', it will return the list ['apple', 'banana'].
    """
    try:
        with open(filename, 'r') as f:
            # Read the content and convert it back to a list using eval
            return eval(f.read())  # Using eval to convert the string back into a Python list
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


def add_arguments_to_json():
    """
    Adds command-line arguments to a list and saves them to a JSON-like file.

    This function does the following:
    1. Retrieves command-line arguments passed to the script.
    2. Loads the existing data from 'add_item.json', if it exists, or initializes an empty list.
    3. Appends the new arguments to the list.
    4. Saves the updated list back to 'add_item.json'.

    The function does not handle exceptions related to invalid arguments and assumes that
    the input is valid.
    
    Example:
        If the script is called as `python3 script.py apple banana`,
        it will add 'apple' and 'banana' to the list in 'add_item.json'.
    """
    import sys  # Importing sys to retrieve command-line arguments
    
    # Get all arguments passed to the script, excluding the script name itself
    arguments = sys.argv[1:]

    # Load existing data from the file or initialize an empty list if the file doesn't exist
    existing_data = load_from_json_file('add_item.json')

    # Append the new arguments to the existing data
    existing_data.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(existing_data, 'add_item.json')


if __name__ == "__main__":
    """
    Main entry point of the script.
    
    Calls the `add_arguments_to_json` function to add command-line arguments to the
    list stored in 'add_item.json'. This function handles reading and writing the file.
    """
    add_arguments_to_json()

