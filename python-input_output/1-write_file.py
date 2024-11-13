#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF-8 encoded)
and returns the number of characters written.

The function `write_file` takes a filename and a text string as input, writes the text
to the specified file (creating or overwriting it if necessary), and returns the
number of characters written to the file.
"""

def write_file(filename="", text=""):
    """
    Writes the given string to a text file (UTF-8 encoded) and returns the number of characters written.

    The function opens the specified file in write mode, writes the provided text to it, and
    then returns the number of characters in the text. If the file doesn't exist, it will be created.
    If the file already exists, its content will be overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
