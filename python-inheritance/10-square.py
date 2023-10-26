#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for creating squares."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """Calculates area"""
        return self.__size ** 2
