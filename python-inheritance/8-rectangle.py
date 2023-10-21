#!/usr/bin/python3

class Rectangle(BaseGeometry):
    """
    A class for creating rectangles.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Attributes:
            __width (int): The width of the rectangle.
            __height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
