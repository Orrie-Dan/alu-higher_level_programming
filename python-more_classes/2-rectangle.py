#!/usr/bin/python3
"""
This module defines a Rectangle class with private attributes for width and height.
The class includes property methods to get and set these attributes, while ensuring
that the width and height are positive integers. It also includes methods to calculate
the area and perimeter of the rectangle.
"""
class Rectangle:
    """
    A class that defines a rectangle by its width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height.

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

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
            If either width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

# Test cases

# Case 1: Rectangle with width 2 and height 4
myrectangle = Rectangle(2, 4)
print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.area()))

# Case 2: Rectangle with width 2 and height 4
myrectangle = Rectangle(2, 4)
print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.perimeter()))

# Case 3: Rectangle with width 10 and height 10
myrectangle = Rectangle(10, 10)
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

# Case 4: Rectangle with width 10 and height 0 (default height)
myrectangle = Rectangle(10)
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

# Case 5: Rectangle with default values (width 0, height 0)
myrectangle = Rectangle()
print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

