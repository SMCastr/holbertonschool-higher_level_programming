#!/usr/bin/python3
""" Module that defines a class Rectangle
that inherits from BaseGeometry."""


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

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
