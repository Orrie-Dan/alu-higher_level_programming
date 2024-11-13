#!/usr/bin/python3

"""
This module contains a function that generates Pascal's Triangle up to the nth row.
Pascal's Triangle is a triangular array of binomial coefficients. Each number in the
triangle is the sum of the two numbers directly above it.

The function `pascal_triangle(n)` returns a list of lists where each list represents
a row in Pascal's Triangle. If n is less than or equal to 0, the function returns
an empty list.

Functions:
    - pascal_triangle(n): Generates Pascal's Triangle up to row n and returns it as a list of lists.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's Triangle up to row n.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists, where each inner list represents a row in Pascal's Triangle.
              If n <= 0, returns an empty list.
              
    Example:
        pascal_triangle(5) -> [
                                [1],
                                [1, 1],
                                [1, 2, 1],
                                [1, 3, 3, 1],
                                [1, 4, 6, 4, 1]
                              ]
    """
    # Base case: If n <= 0, return an empty list
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Generate rows 1 to n-1 (since the first row is already initialized)
    for row_num in range(1, n):
        # Start the row with the first 1
        row = [1]
        
        # Calculate the middle elements using the previous row
        for j in range(1, row_num):
            row.append(triangle[row_num - 1][j - 1] + triangle[row_num - 1][j])
        
        # End the row with the last 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)

    # Return the full Pascal's Triangle
    return triangle

