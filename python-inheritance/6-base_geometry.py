#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
This class is an empty base class for geometry-related classes.
"""

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Overrides the area method to calculate the area of a rectangle."""
        return self.width * self.height

# Create a Rectangle instance
rect = Rectangle(4, 5)
print(rect.area())  # Output: 20

# Attempting to call `area()` on a BaseGeometry object should raise an exception:
# geo = BaseGeometry()
# geo.area()  # This would raise: Exception: area() is not implemented

