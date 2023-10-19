#!/usr/bin/python3
"""
This module defines the Square class with size validation.
"""


class Square:
    """
    The Square class represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes an instance of the Square class with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(3.14)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_5 = Square(-89)
        print(type(my_square_5))
        print(my_square_5.__dict__)
    except Exception as e:
        print(e)
