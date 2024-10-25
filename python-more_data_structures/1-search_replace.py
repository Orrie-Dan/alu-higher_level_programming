#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list with the replaced values
    return [replace if item == search else item for item in my_list]
