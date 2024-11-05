#!/usr/bin/python3
"""
Module that defines a Square class with private attributes 'size' and 'position',
with getter and setter methods, an area method, and a print method that uses the position.
"""

class Square:
    """
    A class that defines a square by its size and position, with getter and setter methods for both,
    an area method, and a method to print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class with a given size and position.

        :param size: Size of the square (defaults to 0)
        :param position: Tuple of 2 integers (defaults to (0, 0))
        :raises TypeError: If size is not an integer, or position is not a tuple of 2 positive integers
        :raises ValueError: If size is less than 0 or position values are not positive
        """
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.

        :return: The position of the square (tuple of 2 positive integers)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute. Validates the position before assigning it.

        :param value: The value to set the position to (tuple of 2 positive integers)
        :raises TypeError: If the value is not a tuple of 2 positive integers
        :raises ValueError: If the values in the tuple are not positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        :return: Area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square in stdout with the character '#'. If size is 0, prints an empty line.
        The position is used to add leading spaces before printing.
        """
        if self.__size == 0:
            print()  # Print an empty line for size 0
        else:
            # Print leading spaces based on position[1]
            for _ in range(self.__position[1]):
                print()  # Newlines based on the vertical position

            for _ in range(self.__size):
                # Print leading spaces before the square on each row based on position[0]
                print(" " * self.__position[0] + "#" * self.__size)

