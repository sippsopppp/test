"""
factorial.py

A simple script to calculate factorial of a non-negative integer.

Usage:
    python factorial.py 5

This will print: 120

You can also import the factorial function in other modules.
"""

import sys
import math


def factorial(n: int) -> int:
    """Return the factorial of a non‑negative integer.

    Args:
        n: Non‑negative integer to calculate factorial for.

    Returns:
        The factorial of n.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    # We could use math.factorial but implement a simple loop for clarity
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <non-negative integer>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    try:
        print(factorial(number))
    except ValueError as e:
        print(e)
        sys.exit(1)

