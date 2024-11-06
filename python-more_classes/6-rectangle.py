#!/usr/bin/python3
"""
Module: rectangle

This module defines a `Rectangle` class which represents a rectangle and provides various
functionalities such as calculating the area, perimeter, and visual representation of the
rectangle using the '#' character. It includes input validation for both the `width` and `height`,
ensuring they are integers and non-negative. The class also keeps track of how many instances of
`Rectangle` have been created and prints a message when an instance is deleted.

Class:
    Rectangle: A class representing a rectangle with validated width and height attributes.

Attributes:
    number_of_instances (int): A class attribute tracking the number of instances of the Rectangle class.
        It is incremented with each new instance and decremented when an instance is deleted.

Usage Example:
    rect1 = Rectangle(4, 5)
    print(rect1.area())       # Returns the area of the rectangle
    print(rect1.perimeter())  # Returns the perimeter of the rectangle
    print(str(rect1))         # Prints the rectangle using '#' characters
    print(repr(rect1))        # Prints a string representation of the rectangle for recreation
    del rect1                 # When deleted, prints: Bye rectangle...
"""

class Rectangle:
    """
    A class representing a rectangle with validated width and height attributes.

    This class provides methods to calculate the area, perimeter, and string representations
    of a rectangle. It includes input validation for the width and height, and tracks the
    number of instances created. Additionally, when an instance is deleted, a message is printed.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
        number_of_instances (int): The number of instances of the Rectangle class.
    """

    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def __del__(self):
        """
        Prints a message when an instance of the rectangle is deleted.

        This method is called when an instance of Rectangle is about to be destroyed.
        It prints the message: 'Bye rectangle...'
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

