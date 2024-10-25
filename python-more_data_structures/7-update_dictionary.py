#!/usr/bin/python3
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
    
    print_sorted_dictionary(new_dict)
    print()  # Adding a newline for clarity

    # Call again to show it works multiple times
    print_sorted_dictionary(new_dict)

