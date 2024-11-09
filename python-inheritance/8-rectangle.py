#!/usr/bin/python3
"""
Module that defines the Rectangle class.
The Rectangle class inherits from BaseGeometry and implements
the __init__ method to validate width and height.
"""

from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""
    
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance, ensuring that width and height are positive integers.
        
        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        # Validate width and height using the inherited integer_validator method
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        # Set private attributes after validation
        self.__width = width
        self.__height = height
