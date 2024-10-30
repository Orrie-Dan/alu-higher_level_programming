#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Print the result
    return result
