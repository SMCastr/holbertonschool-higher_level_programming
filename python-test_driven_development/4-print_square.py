#!/usr/bin/python3
"""
Module to print a square of #
"""


def print_square(size):
    """
    Print a square of '#' characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
