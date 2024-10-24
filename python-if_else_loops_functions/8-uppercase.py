#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end='')  # Convert to uppercase
        else:
            print(char, end='')
    print()  # Print a new line at the end

