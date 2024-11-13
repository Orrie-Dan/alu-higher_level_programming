#!/usr/bin/python3
"""
This module contains a function that reads a text file encoded in UTF-8
and prints its contents to the standard output.

The purpose of this module is to demonstrate basic file reading and
output functionality in Python using the 'with' statement to handle
file opening and closing safely.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to the standard output.

    The function opens the specified file, reads its content, and prints it to the console.
    If no filename is provided, the function defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
