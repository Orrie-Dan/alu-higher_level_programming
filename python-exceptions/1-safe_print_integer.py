#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to print the value using the specified format
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Catch errors related to non-integer types
        return False

