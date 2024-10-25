#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end='')  # No trailing space
            else:
                print("{:d}".format(row[i]), end=' ')
        print()  # Move to the next line after each row

