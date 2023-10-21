#!/usr/bin/python3
class BaseGeometry:
    """
    A class for geometry operations.

    Methods:
        area(self): Raise an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validate the integer value.

    Attributes:
        __width (int): The width of the geometry.
        __height (int): The height of the geometry.
    """
    def __init__(self):
        """
        Initialize an instance of BaseGeometry.
        """
        self.__width = 0
        self.__height = 0

    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): The name of the attribute.
            value: The value to be validated.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
