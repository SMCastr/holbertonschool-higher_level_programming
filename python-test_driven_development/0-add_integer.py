#!/usr/bin/python3

def add_integer(a, b):
    """
    This function takes two integers as input and returns their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    return a + b

# If you have more functions, add them here.
