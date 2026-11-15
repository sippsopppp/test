def multiply(a, b):
    """Return the product of a and b."""
    return a * b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python multiply.py <num1> <num2>")
        sys.exit(1)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        sys.exit(1)
    result = multiply(a, b)
    print(f"{a} * {b} = {result}")

