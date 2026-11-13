def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python add_numbers.py num1 num2")
        sys.exit(1)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        sys.exit(1)
    print(add(a, b))

