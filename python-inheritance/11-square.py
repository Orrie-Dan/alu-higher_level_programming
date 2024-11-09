#!/usr/bin/python3
"""
Module that defines the Square class.
The Square class inherits from Rectangle, validates the size attribute,
and provides its own area and string representation.
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


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    
    def __init__(self, size):
        """Initializes a square with a given size."""
        self.integer_validator("size", size)  # Validate size
        super().__init__(size, size)  # Call the parent constructor with the same size for width and height
    
    def area(self):
        """Calculates the area of the square."""
        return self._Rectangle__width * self._Rectangle__height
    
    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
