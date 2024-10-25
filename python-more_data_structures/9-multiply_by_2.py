#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary

# Example usage
if __name__ == "__main__":
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    result_dict = multiply_by_2(original_dict)
    print(result_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

