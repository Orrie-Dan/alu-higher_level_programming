#!/usr/bin/python3

"""
This module contains a function `matrix_divided` that divides all elements of a matrix
by a given divisor.

The function performs the following checks and validations:
- Ensures the matrix is a list of lists of integers or floats.
- Ensures each row of the matrix has the same size.
- Ensures the divisor is a number (either integer or float) and is not zero.
- Divides each element of the matrix by the divisor and rounds the result to 2 decimal places.
- Returns a new matrix with the divided values.

Raises:
    TypeError: If the matrix is not a list of lists of integers/floats.
    TypeError: If the rows of the matrix are not of equal size.
    TypeError: If the divisor is not a number.
    ZeroDivisionError: If the divisor is zero.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div), rounding the result to 2 decimal places.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The number by which each element of the matrix will be divided.

    Returns:
        list of lists: A new matrix with the divided values, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
                    If each row of the matrix does not have the same size.
                    If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    
    return new_matrix 
if __name__=="__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt") 
