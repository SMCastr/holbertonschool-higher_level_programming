#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base__init__(self):
        """Test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_create(cls, **dictionary):
        """Test the create method of the Base class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        cls.assertisInstance(r2, Rectangle)
        cls.assertEqual(r1, r2)

        cls.assertIsNot(r1, r2)

    def test_save_to_file(cls, list_objs):
        """Test the save_to_file method of the Base class"""
        # save and load a list of retangles
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        cls.assertEqual(list_rectangles_input, list_rectangles_output)

        # save and load a list of Square instances
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square .save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        cls.assertEqual(list_squares_input, list_squares_output)

    def test_load_from_file(cls):
        """Test the load_from_file method of the Base class"""
        # load a list of Rectangle instances from a file
        list_rectangles = Rectangle.load_from_file()
        cls.assertIsInstance(list_rectangles, list)

        for rectangle in list_rectangles:
            cls.assertIsInstance(rectangle, Rectangle)

        # load a list of Square instances from a file
        list_squares = Square.load_from_file()
        cls.assertIsInstance(list_squares, list)

        for square in list_squares:
            cls.assertIsInstance(square, Square)

    def test_create(self):
        """Test the create method of the Base class"""
         # Test creating a Rectangle object
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

         # Test creating a Square object
        square_dict = {'id': 2, 'size': 6, 'x': 7, 'y': 8}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_save_to_file(self):
        """Test the save_to_file method of the Base class"""
         # Test with a list of Rectangle objects
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Base.save_to_file(list_rectangles)
        with open("Rectangle.json", "r") as file:
        self.assertEqual(file.read(
        ), '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')

         # Test with a list of Square objects
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        list_squares = [s1, s2]
        Base.save_to_file(list_squares)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(
            ), '[{"id": 3, "size": 10, "x": 2, "y": 8}, {"id": 4, "size": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
         """Test the load_from_file method of the Base class"""
         # Test with a list of Rectangle objects
         list_rectangles = Base.load_from_file()
         self.assertEqual(list_rectangles, [{'y': 8, 'x': 2, 'id': 1, 'width': 10, 'height': 7}, {
                          'y': 0, 'x': 0, 'id': 2, 'width': 2, 'height': 4}])

         # Test with a list of Square objects
         list_squares = Base.load_from_file()
         self.assertEqual(list_squares, [{'id': 3, 'size': 10, 'x': 2, 'y': 8}, {
                          'id': 4, 'size': 2, 'x': 0, 'y': 0}])

    def test_to_json_string(self):
         """Test the to_json_string method of the Base class"""
         # Test with a list of Rectangle objects
         r1 = Rectangle(10, 7, 2, 8)
         r2 = Rectangle(2, 4)
         list_rectangles = [r1, r2]
         json_string = Base.to_json_string(list_rectangles)
         expected_string = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
         self.assertEqual(json_string, expected_string)

         # Test with a list of Square objects
         s1 = Square(10, 2, 8)
         s2 = Square(2)
         list_squares = [s1, s2]
         json_string = Base.to_json_string(list_squares)
         expected_string = '[{"id": 3, "size": 10, "x": 2, "y": 8}, {"id": 4, "size": 2, "x": 0, "y": 0}]'
         self.assertEqual(json_string, expected_string)

    def test_from_json_string(self):
         """Test the from_json_string method of the Base class"""
         # Test with a JSON string
         json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, {"id": 2, "size": 6, "x": 7, "y": 8}]'
         list_dicts = Base.from_json_string(json_string)
         expected_list = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5},
                          {'id': 2, 'size': 6, 'x': 7, 'y': 8}]
         self.assertEqual(list_dicts, expected_list)

         # Test with an empty string
         empty_string = ''
         list_dicts = Base.from_json_string(empty_string)
         expected_list = []
         self.assertEqual(list_dicts, expected_list)

         # Test with None
         list_dicts = Base.from_json_string(None)
         expected_list = []
         self.assertEqual(list_dicts, expected_list)


if __name__ == '__main__':
    unittest.main()
