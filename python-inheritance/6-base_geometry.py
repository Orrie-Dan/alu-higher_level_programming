#!/usr/bin/python3
"""
Module: base_geometry.py

This module contains a class `BaseGeometry`, which serves as a base class for geometric shapes.
It defines the method `area()` that should be implemented by subclasses to calculate the area of a specific shape.
"""

class BaseGeometry:
    """
    Class: BaseGeometry

    A base class for geometric shapes. Provides a placeholder method `area()` that raises an exception 
    if called directly. Subclasses are expected to override this method to provide their own implementation.

    Methods:
        area(self): Raises an exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Method: area

        Raises an Exception indicating that the area method has not been implemented.

        Raises:
            Exception: If called directly from BaseGeometry without being overridden in a subclass.
        """
        raise Exception("area() is not implemented")

