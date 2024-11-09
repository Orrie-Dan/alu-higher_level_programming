#!/usr/bin/python3
"""
Module that defines the Square class.
The Square class inherits from Rectangle and validates the size attribute.
"""

from rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""
    
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.
        
        Parameters:
        - size (int): The size of the square.
        """
        # Validate the size using the inherited integer_validator method
        self.integer_validator("size", size)
        
        # Call the parent class constructor with the same size for width and height
        super().__init__(size, size)
