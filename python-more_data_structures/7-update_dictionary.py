#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the given key and value
    a_dictionary[key] = value

# Example usage
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Update an existing key
    update_dictionary(my_dict, 'b', 5)
    print(my_dict)  # Output: {'a': 1, 'b': 5, 'c': 3}

    # Add a new key
    update_dictionary(my_dict, 'd', 4)
    print(my_dict)  # Output: {'a': 1, 'b': 5, 'c': 3, 'd': 4}

