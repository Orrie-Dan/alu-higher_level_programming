#!/usr/bin/python3
"""
Module that defines a Rectangle class.

The class defines a rectangle with private attributes for width and height.
It includes getters and setters with validation to ensure that:
  - The width and height are integers.
  - The width and height are greater than or equal to 0.
  
Attributes:
    width (int): The width of the rectangle, must be a non-negative integer.
    height (int): The height of the rectangle, must be a non-negative integer.
"""

class Rectangle:
    """
    A class that defines a rectangle by its width and height.

    Methods:
        __init__(self, width=0, height=0): Initializes the rectangle with width and height.
        width(self): Returns the width of the rectangle.
        width(self, value): Sets the width of the rectangle with validation.
        height(self): Returns the height of the rectangle.
        height(self, value): Sets the height of the rectangle with validation.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with a width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
