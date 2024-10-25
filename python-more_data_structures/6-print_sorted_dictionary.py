#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")

# Example usage:
if __name__ == "__main__":
    my_dict = {
        "b": 1,
        "a": 2,
        "c": [1, 2, 3],
        "d": {"nested_key": 5}
    }
    print_sorted_dictionary(my_dict)

