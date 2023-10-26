#!/usr/bin/python3
""" Geometry Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for creating squares.
    """
    def __init__(self, size):
        """
        Initialize a square with the given size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
