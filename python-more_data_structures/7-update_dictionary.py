#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:  # Handle None input gracefully
        return

    # Sort the keys and print key-value pairs
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")

# Example usage
if __name__ == "__main__":
    new_dict = {
        'a': 'A',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
    }

    print_sorted_dictionary(new_dict)  # Print the original dictionary
    print()  # Adding a newline for clarity

    # Adding an additional key-value pair
    new_dict['xx'] = 'xx'
    print_sorted_dictionary(new_dict)  # Print after adding new key

