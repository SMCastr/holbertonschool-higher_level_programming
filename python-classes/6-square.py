#!/usr/bin/python3
"""
This module defines the Square class with size validation, area calculation,
printing functionality, and position attribute.
"""


class Square:
    """
    The Square class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of the Square class with a given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains negative values.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character # and uses the position attribute.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3, (1, 1))
    print(my_square.size)
    print(my_square.area())
    print(my_square.position)

    my_square = Square(3, "Position")
    my_square = Square(3, (1, ))
    my_square = Square(3, (1, -3))
    my_square = Square(3, (1, "3"))

    my_square = Square(3)
    my_square.my_print()

    my_square = Square(3, (0, 0))
    my_square.my_print()

    my_square = Square(3, (1, 0))
    my_square.my_print()

    my_square = Square(3, (0, 1))
    my_square.my_print()

    my_square = Square(3, (1, 1))
    my_square.my_print()

    my_square = Square(5, (3, 2))
    my_square.my_print()

    my_square = Square(0, (10, 3))
    my_square.my_print()
