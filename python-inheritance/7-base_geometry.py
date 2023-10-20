#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Calculate the area - raises an exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if value is an integer greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
