#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle.
"""


class Rectangle:
    """
    Define a Rectangle with width and height attributes.
    """

    number_of_instances = 0  # Class attribute
    print_symbol = "#"  # Class attribute

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle with optional width and height.
        Increment the number_of_instances when an instance is created.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] 
                         for i in range(self.__height))
    def __repr__(self):
        """
        Return a string representation of the rectangle to recreate the object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        Decrement the number_of_instances when an instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

# Additional test cases


if __name__ == '__main__':
    my_rectangle1 = Rectangle(8, 4)
    print(my_rectangle1)

    Rectangle.print_symbol = "C"
    my_rectangle1 = Rectangle(8, 4)
    print(my_rectangle1)

    Rectangle.print_symbol = "C"
    my_rectangle1 = Rectangle(8, 4)
    my_rectangle2 = Rectangle(2, 1)
    print(my_rectangle2)

    Rectangle.print_symbol = "C"
    my_rectangle1 = Rectangle(8, 4)
    my_rectangle1.print_symbol = "H"
    print(my_rectangle1)

    my_rectangle2 = Rectangle(2, 1)
    print(my_rectangle2)

    my_rectangle1 = Rectangle(8, 4)
    my_rectangle1.print_symbol = "H"
    print(my_rectangle1)

    Rectangle.print_symbol = "K"
    my_rectangle2 = Rectangle(2, 1)
    print(my_rectangle2)

    my_rectangle1 = Rectangle(8, 4)
    my_rectangle1.print_symbol = 89
    print(my_rectangle1)

    my_rectangle1 = Rectangle(8, 4)
    my_rectangle1.print_symbol = ["Holberton", "School"]
    print(my_rectangle1)
