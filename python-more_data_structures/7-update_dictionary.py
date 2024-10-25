#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the given key and value
    a_dictionary[key] = value

# Example usage
if __name__ == "__main__":
    my_dict = {'a': 'A', 'b': 'b', 'c': 'c'}
    
    # Update an existing key
    update_dictionary(my_dict, 'a', 'Alpha')
    print_sorted_dictionary(my_dict)  # After updating 'a'
    
    # Add a new key
    update_dictionary(my_dict, 'd', 'd')
    print_sorted_dictionary(my_dict)  # After adding 'd'

