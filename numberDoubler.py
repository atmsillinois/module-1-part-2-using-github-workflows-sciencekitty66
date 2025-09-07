# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Alison Chatham

"""
This script takes a number as input, doubles it, and prints the result.
"""


def double_number(number):
    """Return twice the given number.

    Args:
        number (float): The number to double

    Returns:
        float: Twice the input number
    """
    return number * 2


def main():
    """Run the number doubler"""
    try:
        value = float(input("Enter a number: "))
        result = double_number(value)
        print(f"\nYou entered: {value}")
        print(f"Doubled value: {result}")
    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()