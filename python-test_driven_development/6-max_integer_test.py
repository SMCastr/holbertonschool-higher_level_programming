#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of positive integers, different order
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test with a list of repeated values
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test with an empty list
        self.assertIsNone(max_integer([])

        # Test with a large list of integers
        self.assertEqual(max_integer(list(range(100000, 1, -1)), 100000)
        self.assertEqual(max_integer(list(range(100000, 200000)), 199999)

if __name__ == '__main__':
    unittest.main()
