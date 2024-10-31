#!/usr/bin/python3
"""
Module for representing a square.
"""

class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance with a given size."""
        self.__size = size  # Private instance attribute
        self.dict_ = {}     # Public attribute

# Usage example
if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))  # Expected output: <class '__main__.Square'>
    print(mysquare.dict_)   # Expected output: {}

    mysquare = Square(89)
    print(type(mysquare))  # Expected output: <class '__main__.Square'>
    print(mysquare.dict_)   # Expected output: {}

    # Testing access to private attribute
    try:
        print(mysquare.__size)
    except Exception as e:
        print(e)  # Expected output: AttributeError

    try:
        print(mysquare._Square__size)
    except Exception as e:
        print(e)  # Expected output: AttributeError
