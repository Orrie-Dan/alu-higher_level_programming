#!/usr/bin/python3
"""
This module contains a function `text_indentation` that processes a given
text string and prints it with two new lines after each of the following
characters: '.', '?', and ':'. The function also ensures that no extra
spaces are added at the beginning or end of each printed line.

Function:
    - text_indentation(text): Takes a string and prints it with two
      newlines after '.', '?', and ':'. It raises a TypeError if the 
      input is not a string.
"""

def text_indentation(text):
    """Prints text with two new lines after '.', '?', and ':' characters."""
    
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Loop through each character in the string and process accordingly
    new_text = ""
    for char in text:
        # Add the character to the new string
        new_text += char
        
        # If we encounter '.', '?', or ':', add two new lines
        if char in ['.', '?', ':']:
            new_text += '\n\n'
    
    # Print the final processed text, making sure no leading/trailing spaces
    # appear at the beginning or end of the printed lines
    print(new_text.strip())

