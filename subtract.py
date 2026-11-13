#!/usr/bin/env python3

import argparse


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def main():
    parser = argparse.ArgumentParser(description='Subtract two numbers.')
    parser.add_argument('a', type=float, help='first number')
    parser.add_argument('b', type=float, help='second number')
    args = parser.parse_args()
    result = subtract(args.a, args.b)
    print(f"{args.a} - {args.b} = {result}")


if __name__ == "__main__":
    main()

