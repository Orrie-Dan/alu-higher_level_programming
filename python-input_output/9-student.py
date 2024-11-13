#!/usr/bin/python3

"""
This class represents a Student. The student has three public attributes:
first_name, last_name, and age. The class includes a method `to_json` which
returns a dictionary representation of the student object for serialization.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the student instance.

        Returns:
            dict: A dictionary with the student's first_name, last_name, and age.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Student class
    student = Student("John", "Doe", 20)

    # Get the dictionary representation of the student
    student_dict = student.to_json()

    # Print the dictionary
    print(student_dict)

