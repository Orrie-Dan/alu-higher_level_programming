#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end='')  # Print the integer
                count += 1
    except IndexError:
        pass  # Ignore if x exceeds the length of my_list
    print()  # Move to the next line after printing
    return count

