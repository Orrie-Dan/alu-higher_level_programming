#!/usr/bin/python3
"""
Module defining the BaseGeometry class.
This class serves as a base for other geometry-related classes.
"""

class BaseGeometry:
    """A base class for geometry objects."""
    
    def area(self):
        """Raises an exception indicating that the method is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        
        Parameters:
        - name (str): The name of the variable (for error messages).
        - value (int): The value to be validated.
        
        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

