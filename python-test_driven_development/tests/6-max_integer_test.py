#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Test for max at the end")

        # Test with a list of integers (unordered)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4, "Test for max at the beginning")

        # Test with an empty list
        self.assertIsNone(max_integer([]), "Test for list is empty")

        # Test with a single integer
        self.assertEqual(max_integer([7]), 7, "Test for list of one element")

        # Test with a list containing only negative integers
        self.assertEqual(max_integer([-5, -3, -9, -1), -1, "Test for only negative numbers in the list")

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-5, 0, 5, 3, -9, 2, 1), 5, "Test for max in the middle")

        # Test with a list of a large number of integers
        self.assertEqual(max_integer(list(range(1, 10001)), 10000, "Test for 'max at the end'")

    def test_empty_list(self):
        # Test an empty list
        self.assertIsNone(max_integer([]), "Test for list is empty")

    def test_floats(self):
        # Test with a list of floats
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4, "Test for floats")

        # Test with mixed integers and floats
        self.assertEqual(max_integer([1.1, 2, 3.3, 4]), 4, "Test for mixed types")

    def test_strings(self):
        # Test with a list of strings
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"], "Test for strings")

    def test_mixed_types(self):
        # Test with a list of mixed data types
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3, "4"], "Test for mixed types")

if __name__ == '__main__':
    unittest.main()
