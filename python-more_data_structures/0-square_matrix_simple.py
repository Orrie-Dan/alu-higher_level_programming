#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix using a list comprehension
    return [[item ** 2 for item in row] for row in matrix]
