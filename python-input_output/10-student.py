#!/usr/bin/python3

"""
This class represents a Student. The student has three public attributes:
first_name, last_name, and age. The class includes a method `to_json` which
returns a dictionary representation of the student object, optionally filtering
attributes based on the provided list `attrs`.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance.

        If attrs is provided, only attributes listed in attrs will be included
        in the dictionary. Otherwise, all attributes will be returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve from the
                                     student instance. Defaults to None.

        Returns:
            dict: A dictionary containing the selected attributes.
        """
        # If attrs is None, return all attributes
        if attrs is None:
            return self.__dict__

        # Create a dictionary with only the specified attributes
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result


