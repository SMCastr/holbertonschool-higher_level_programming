#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of integers (unordered)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a single integer
        self.assertEqual(max_integer([7]), 7)

        # Test with a list containing only negative integers
        self.assertEqual(max_integer([-5, -3, -9, -1]), -1)

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-5, 0, 5, 3, -9, 2, 1]), 5)

        # Test with a list of a large number of integers
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

    def test_empty_list(self):
        # Test an empty list
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        # Test with a list of floats
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

        # Test with mixed integers and floats
        self.assertEqual(max_integer([1.1, 2, 3.3, 4]), 4)

    def test_strings(self):
        # Test with a list of strings
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_mixed_types(self):
        # Test with a list of mixed data types
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3, "4"])

if __name__ == '__main__':
    unittest.main()
