#!/usr/bin/env python3

# Simple program to multiply 7 numbers
# Usage: python3 multiply_seven.py num1 num2 num3 num4 num5 num6 num7
import sys

if len(sys.argv) != 8:
    print(f"Usage: {sys.argv[0]} num1 num2 num3 num4 num5 num6 num7")
    sys.exit(1)

numbers = [float(arg) for arg in sys.argv[1:]]
product = 1
for n in numbers:
    product *= n
print(product)

