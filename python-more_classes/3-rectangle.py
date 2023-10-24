#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Define a Rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.__width is 0 or self.__height is 0:
            return ""
        string_rep = ""
        for i in range(self.__height):
            string_rep += "#" * self.__width
            if i is not self.__height - 1:
                string_rep += "\n"
        return string_rep