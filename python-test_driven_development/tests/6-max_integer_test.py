#!/usr/bin/python3
"""
This module contains a function `text_indentation` that prints the given 
text with two new lines after each occurrence of '.', '?', and ':'. 
It ensures there are no leading or trailing spaces in the printed lines 
and raises a TypeError if the input is not a string.
"""

def text_indentation(text):
    """Prints the given text with two new lines after '.', '?', and ':'"""
    
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Loop through the text to process each character
    i = 0
    while i < len(text):
        # Print the current character
        print(text[i], end="")
        
        # Check if the current character is '.', '?', or ':'
        if text[i] in ['.', '?', ':']:
            # Print two new lines
            print("\n")
            # Skip any leading spaces after the punctuation
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        
        i += 1

