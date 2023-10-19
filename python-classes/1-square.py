#!/usr/bin/python3
"""
This module defines the Square class with a private attribute size.

The Square class is used to represent a square. It has a private attribute
size, which is initialized during object creation.
"""


class Square:
    """
    The Square class represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes an instance of the Square class with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        print(mysquare.size)
    except Exception as e:
        print(e)

    try:
        print(mysquare._size)
    except Exception as e:
        print(e)
