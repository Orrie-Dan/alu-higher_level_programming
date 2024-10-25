#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the given key and value
    a_dictionary[key] = value

# Example usage:
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2}

    # Update an existing key
    update_dictionary(my_dict, 'a', 3)
    print(my_dict)  # Output: {'a': 3, 'b': 2}

    # Add a new key
    update_dictionary(my_dict, 'c', 4)
    print(my_dict)  # Output: {'a': 3, 'b': 2, 'c': 4}

