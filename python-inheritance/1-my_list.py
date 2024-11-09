#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
The MyList class adds a method `print_sorted()` that prints the list in sorted
order without modifying the original list.

Usage:
    - You can create an instance of MyList and use it just like a regular list.
    - The `print_sorted()` method will print the list sorted in ascending order.
"""

class MyList(list):
    """
    A subclass of list that adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))

