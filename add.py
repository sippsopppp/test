"""Simple multiplication program.

This script prompts the user for two numeric inputs, multiplies them,
and prints the result in a clear statement.
"""

def main():
    try:
        a_str = input("Enter the first number: ")
        b_str = input("Enter the second number: ")
        # Convert to float for general numeric input
        a = float(a_str)
        b = float(b_str)
        result = a * b
        # If result is an integer, display as int
        if result.is_integer():
            result_display = int(result)
        else:
            result_display = result
        print(f"Result: {result_display}")
    except ValueError:
        print("Error: please enter valid numeric values.")

if __name__ == "__main__":
    main()

