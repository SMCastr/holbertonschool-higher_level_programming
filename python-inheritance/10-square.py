#!/usr/bin/python3

class Square(Rectangle):
    """
    A class for creating squares.

    Args:
        size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initialize a square with the given size.

        Attributes:
            __size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
