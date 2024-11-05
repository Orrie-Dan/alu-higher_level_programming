#!/usr/bin/python3
"""
Module that defines a Square class with a private attribute 'size' and methods for validation and area calculation.
"""

class Square:
    """
    A class that defines a square by its size, with validation on size and an area method.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with a given size.

        :param size: Size of the square (defaults to 0)
        :raises TypeError: If size is not an integer
        :raises ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size  # Private instance attribute

    def area(self):
        """
        Returns the area of the square.

        :return: Area of the square (size * size)
        """
        return self.__size * self.__size  # Area calculation
