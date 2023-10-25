#!/usr/bin/python3
""" Geometry Module"""


class BaseGeometry:
    """
    A class for geometry operations.
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
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
