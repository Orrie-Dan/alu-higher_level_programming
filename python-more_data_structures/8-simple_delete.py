#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Remove the key from the dictionary if it exists
    if key in a_dictionary:
        del a_dictionary[key]

# Example usage
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Delete an existing key
    simple_delete(my_dict, 'b')
    print(my_dict)  # Output: {'a': 1, 'c': 3}

    # Attempt to delete a non-existing key
    simple_delete(my_dict, 'd')
    print(my_dict)  # Output: {'a': 1, 'c': 3} (unchanged)

