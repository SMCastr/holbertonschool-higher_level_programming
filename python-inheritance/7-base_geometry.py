#!/usr/bin/python3
""" Geometry Module"""


class BaseGeometry:
    """
    A class for geometry operations.
    """


    def area(self):
        """
        Raise an Exception with the
        message "area() is not implemented".
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
        else:
            self.name = name
            self.value = value
