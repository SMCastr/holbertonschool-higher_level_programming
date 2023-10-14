#!/usr/bin/python3
class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """String representation for recreation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method"""
        print("Bye rectangle...")

my_rectangle = Rectangle(2, 4)
print(my_rectangle)

# Try to change width and catch the exception
try:
    my_rectangle.width = 12
except Exception as e:
    print("[{}] {}".format(e.__class__.__name, e))
