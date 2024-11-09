#!/usr/bin/python3
"""
Module that defines the Square class.
The Square class inherits from Rectangle, validates the size attribute,
and provides its own area and string representation.
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
    
    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
