#!/usr/bin/python3
class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance with a given size."""
        self.__size = size  # Private instance attribute

# Usage example
if __name__ == "__main__":
    mysquare = Square(5)
    # Note: The size is private and cannot be accessed directly
    print(type(mysquare))  

