#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the given key and value
    a_dictionary[key] = value

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return  # Handle the case where the input is None

    # Sort the keys of the dictionary and print key-value pairs
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")

# Example usage
if __name__ == "__main__":
    new_dict = {
        "b": "b",
        "a": "A",
        "c": "c",
        "e": "e",
        "d": "d",
    }

    print_sorted_dictionary(new_dict)  # Print the original dictionary
    print()  # Adding a newline for clarity

    # Update an existing key
    update_dictionary(new_dict, 'a', 'Alpha')
    print_sorted_dictionary(new_dict)  # Print after update

    # Add a new key
    update_dictionary(new_dict, 'f', 'f')
    print_sorted_dictionary(new_dict)  # Print after adding new key

