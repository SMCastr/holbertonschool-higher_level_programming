#!/usr/bin/python3

class BaseGeometry:
    """
    A class for geometry operations.

    Methods:
        area(self): Raise an Exception with the message "area() is not implemented".
    """
    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
