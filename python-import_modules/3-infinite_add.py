#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total = 0

    # Iterate through the arguments (excluding the script name)
    for arg in sys.argv[1:]:
        total += int(arg)  # Convert to integer and add to total

    print(total)  # Print the result

