#!/usr/bin/env python3
"""Program that multiplies 10 numbers."""

import sys

def multiply_numbers(nums):
    result = 1
    for n in nums:
        result *= n
    return result

if __name__ == "__main__":
    if len(sys.argv) != 11:
        print("Usage: python multiply.py n1 n2 ... n10")
        sys.exit(1)
    numbers = [float(arg) for arg in sys.argv[1:]]
    print(multiply_numbers(numbers))

