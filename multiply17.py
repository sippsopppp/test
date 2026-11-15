"""
Program that adds 17 numbers.
"""

def sum_seventeen(nums):
    if len(nums) != 17:
        raise ValueError("Expected 17 numbers")
    return sum(nums)

if __name__ == "__main__":
    numbers = [i for i in range(1, 18)]
    print(f"The sum of numbers 1..17 is: {sum_seventeen(numbers)}")

