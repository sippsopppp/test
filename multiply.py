#!/usr/bin/env python3
"""Simple multiplication program.

This script reads two numbers from command line arguments and prints
their product. If no arguments are supplied it prompts the user.
"""

import sys


def main():
    args = sys.argv[1:]
    if len(args) == 2:
        try:
            a = float(args[0])
            b = float(args[1])
        except ValueError:
            print("Error: both arguments must be numbers.")
            sys.exit(1)
    else:
        # interactive mode
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Error: invalid input.")
            sys.exit(1)
    product = a * b
    # print as integer if both inputs are integers
    if a.is_integer() and b.is_integer():
        print(int(product))
    else:
        print(product)

if __name__ == "__main__":
    main()

