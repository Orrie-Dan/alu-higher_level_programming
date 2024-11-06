#!/usr/bin/python3
"""
Module: Rectangle

This module defines a class representing a rectangle with various functionalities such as
calculating its area, perimeter, and providing string representations. The class includes
input validation to ensure that the width and height of the rectangle are positive integers.

Classes:
    Rectangle: A class representing a rectangle, with attributes for width and height.

Usage Example:
    rect = Rectangle(4, 5)
    print(rect.area())       # Output: 20
    print(rect.perimeter())  # Output: 18
    print(str(rect))         # Output: A rectangle printed using '#' characters.
    print(repr(rect))        # Output: Rectangle(4, 5)
"""

class Rectangle:
    """
    A class representing a rectangle.

    The Rectangle class allows you to create a rectangle with a specified width and height.
    It includes methods to calculate the area, perimeter, and string representations of the
    rectangle.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle using '#' characters.
        __repr__(): Returns a string that can be used to recreate the rectangle.

    Exceptions:
        TypeError: Raised if the width or height is not an integer.
        ValueError: Raised if the width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).

        If either the width or height is 0, returns 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: A string representing the rectangle.

        If either the width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreating it.

        Returns:
            str: A string that can be used to recreate the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
