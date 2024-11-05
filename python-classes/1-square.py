#!/usr/bin/python3
"""
Module that defines a Square class with a private attribute 'size'.
"""

class Square:
    """
    A class that defines a square by its size.
    The size attribute is private.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class with a given size.
        
        The size attribute is private (denoted by the __ prefix).
        """
        self.__size = size  # Private instance attribute
