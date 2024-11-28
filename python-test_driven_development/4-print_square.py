#!/usr/bin/python3
"""
This module contains a function `print_square` that prints a square of 
# characters based on the given size. It includes error handling to ensure
that the size is a valid integer, is non-negative, and is not a float 
less than 0.

Function:
    - print_square(size): Prints a square with # characters of 
      the specified size. Raises exceptions for invalid input.
"""
def print_square(size):
    """Prints a square with the character #."""
    
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Check if size is a float and less than 0 (TypeError if it's a negative float)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    # Print the square
    for i in range(size):
        print('#' * size)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
