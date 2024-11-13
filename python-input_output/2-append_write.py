#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file (UTF-8 encoded) 
and returns the number of characters added.

The function `append_write` takes a filename and a text string as input, appends the text 
to the specified file (creating the file if necessary), and returns the number of characters 
that were added to the file.
"""

def append_write(filename="", text=""):
    """
    Appends the given string to a text file (UTF-8 encoded) and returns the number of characters added.
    
    The function opens the specified file in append mode, adds the provided text to it, and 
    then returns the number of characters in the text. If the file doesn't exist, it will be created.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
