#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1  # Exclude the script name

    if num_arguments == 0:
        print("Number of arguments: 0.")
    else:
        argument_word = "argument" if num_arguments == 1 else "arguments"
        print("{} {}:".format(num_arguments, argument_word))
        
        # Print each argument
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

