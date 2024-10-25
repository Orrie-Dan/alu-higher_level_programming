#!/usr/bin/python3

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")
 cases = [
        (1, 2),
        (10, 30),
        (-10, 30),
        (-10, -30),
        (5, "H")
    ]

    for a, b in cases:
        try:
            result = add(a, b)
            print(f"{a} - {b} = {result}")
        except TypeError:
            print(f"{a} - {b} = Error: Unsupported operation")
