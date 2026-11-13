"""Simple calculator program.

This script implements a basic command‑line calculator that can
perform addition, subtraction, multiplication, and division.
It supports integer and float operands.
"""

import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <op> <num1> <num2>")
        print("Operations: add, sub, mul, div")
        sys.exit(1)

    op, num1, num2 = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(num1)
        b = float(num2)
    except ValueError:
        print("Both operands must be numeric.")
        sys.exit(1)

    try:
        if op == "add":
            result = add(a, b)
        elif op == "sub":
            result = subtract(a, b)
        elif op == "mul":
            result = multiply(a, b)
        elif op == "div":
            result = divide(a, b)
        else:
            print("Unsupported operation. Use add, sub, mul, div.")
            sys.exit(1)
    except ZeroDivisionError as e:
        print(e)
        sys.exit(1)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()

