#!/usr/bin/python3
""" Geometry Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class for creating rectangles.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
