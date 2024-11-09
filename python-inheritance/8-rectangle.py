#!/usr/bin/python3
"""
Module that defines the Rectangle class.
The Rectangle class inherits from BaseGeometry and implements
the __init__ method to validate width and height.
"""

class BaseGeometry:
    """Base class for geometry operations."""
    
    def area(self):
        """Raises an exception when called, to be overridden in child classes."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry and represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with the given width and height.

        Arguments:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

        Both width and height are validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute
    
    def area(self):
        """Calculates the area of the rectangle.

        Returns:
        int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height
    
    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

