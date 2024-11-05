#!/usr/bin/python3
"""
Module that defines a Square class with a private attribute 'size',
getter and setter methods, an area method, and a print method.
"""

class Square:
    """
    A class that defines a square by its size, with getter and setter methods for the size attribute,
    an area method, and a method to print the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with a given size.

        :param size: Size of the square (defaults to 0)
        :raises TypeError: If size is not an integer
        :raises ValueError: If size is less than 0
        """
        self.size = size  # Using the setter to validate the size

    @property
    def size(self):
        """
        Getter for the size attribute.

        :return: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. Validates the size before assigning it.

        :param value: The value to set the size to
        :raises TypeError: If the value is not an integer
        :raises ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private attribute

    def area(self):
        """
        Returns the area of the square.

        :return: Area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square in stdout with the character '#'. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()  # Print an empty line for size 0
        else:
            for i in range(self.__size):
                print('#' * self.__size)  # Print a row of '#' characters
