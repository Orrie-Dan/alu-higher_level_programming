#!/usr/bin/python3
def islower(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

# Test cases
test_cases = ['a', 'z', 'A', 'Z', '4', '!']

for char in test_cases:
    result = islower(char)
    print(f"Character: '{char}' - islower: {result}")

