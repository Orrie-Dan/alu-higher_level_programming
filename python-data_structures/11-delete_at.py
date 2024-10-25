#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the list unchanged if index is invalid

    # Create a new list without the element at the specified index
    return my_list[:idx] + my_list[idx + 1:]

