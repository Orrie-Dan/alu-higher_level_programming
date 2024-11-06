#!/usr/bin/python3
"""
Module: rectangle

This module defines a `Rectangle` class representing a rectangle. The class provides methods to
calculate the area, perimeter, and string representation of the rectangle, with customizable
symbols for drawing the rectangle. It includes input validation for both `width` and `height`
ensuring they are integers and non-negative. Additionally, the class tracks the number of instances
created, provides a string representation, and prints a message when an instance is deleted.
There is also a static method to compare two rectangles based on their area and a class method to
create a square.

Class:
    Rectangle: A class representing a rectangle with validated width, height, and customizable symbol for drawing.

Attributes:
    number_of_instances (int): A class attribute that tracks the number of instances of the `Rectangle` class.
        It is incremented with each new instance and decremented when an instance is deleted.
    print_symbol (any): A class attribute that stores the symbol used to print the rectangle. It can be any type,
        but defaults to `#`.

Usage Example:
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 7)
    print(rect1.area())       # Returns the area of the rectangle
    print(rect1.perimeter())  # Returns the perimeter of the rectangle
    print(str(rect1))         # Prints the rectangle using the symbol(s) in `print_symbol`
    print(repr(rect1))        # Prints a string representation of the rectangle for recreation
    del rect1                 # When deleted, prints: Bye rectangle...

    bigger = Rectangle.bigger_or_equal(rect1, rect2)
    print(bigger)             # Compares and prints the rectangle with the largest area

    square = Rectangle.square(4)   # Creates a square with width and height of 4
    print(square)                   # Prints the square
"""
class Rectangle:
    """
    A class representing a rectangle with validated width, height, and customizable symbol for drawing.
    This class provides methods to calculate the area, perimeter, and string representations of
    a rectangle. It includes input validation for the width and height, ensures proper instance tracking,
    and supports customizable drawing symbols. Additionally, the class provides a static method to compare
    two rectangles based on their area and return the larger one. It also provides a class method to create
    a square where width equals height.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
        number_of_instances (int): The number of instances of the Rectangle class.
        print_symbol (any): The symbol used to draw the rectangle. Can be any type, default is `#`.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        """Gets the width of the rectangle."""
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
        """Gets the height of the rectangle."""
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
        """Calculates and returns the area of the rectangle (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle (2 * (width + height)).

        If either the width or height is 0, returns 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the symbol stored in print_symbol.

        If either the width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle for recreating it."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance of the rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles and returns the one with the largest area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area. If both have the same area, returns rect_1.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance where width and height are equal (i.e., a square).

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return cls(size, size)

