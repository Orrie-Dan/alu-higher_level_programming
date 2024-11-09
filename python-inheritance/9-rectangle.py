#!/usr/bin/python3
"""
Module that defines the Rectangle class.
The Rectangle class inherits from BaseGeometry, validates width and height,
calculates the area, and provides a string representation.
"""

class BaseGeometry:
    """Base class for geometry-related operations."""
    
    def area(self):
        """Raises an exception if called directly. To be implemented by subclasses."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initializes a Rectangle with width and height."""
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        
        self.__width = width  # Private width attribute
        self.__height = height  # Private height attribute
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

