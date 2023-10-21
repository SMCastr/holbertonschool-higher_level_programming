from rectangle import Rectangle

class Square_tow(Rectangle):
    """
    A class named Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes an instance of Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
