# Python Test-Driven Development

This repository contains a set of Python scripts and their corresponding test files created as part of a Test-Driven Development (TDD) exercise. Each script addresses specific programming tasks and is tested using the Doctest and Unittest frameworks.

## Scripts

### 0-add_integer.py

This script provides a function `add_integer(a, b=98)` that adds two integers. It raises a `TypeError` exception if the input arguments `a` and `b` are not integers or floats. The function first casts the input arguments to integers if they are floats and returns the addition result as an integer.

### 0-add_integer.txt

This test file contains test cases for the `add_integer` function. It ensures that the function handles various scenarios, including valid inputs, invalid inputs, and optional arguments.

### 2-matrix_divided.py

The script `2-matrix_divided.py` defines a function `matrix_divided(matrix, div)` that divides all elements of a matrix by a given number `div`. The function checks for valid input types and dimensions, and it rounds the results to two decimal places. It returns a new matrix with the results.

### 2-matrix_divided.txt

This test file contains test cases for the `matrix_divided` function. It ensures that the function correctly divides the matrix and handles different scenarios, such as valid and invalid input types and dimensions.

### 3-say_my_name.py

The script `3-say_my_name.py` includes a function `say_my_name(first_name, last_name="")` that prints "My name is <first name> <last name>". It raises a `TypeError` exception if the input arguments `first_name` and `last_name` are not strings.

### 3-say_my_name.txt

This test file contains test cases for the `say_my_name` function. It verifies that the function correctly prints the name and handles different scenarios, including valid and invalid inputs.

### 4-print_square.py

The script `4-print_square.py` defines a function `print_square(size)` that prints a square with the character `#`. The function validates the size input, raising `TypeError` and `ValueError` exceptions if necessary.

### 4-print_square.txt

This test file contains test cases for the `print_square` function. It ensures that the function correctly prints squares of different sizes and handles various scenarios, including valid and invalid input types.

### 5-text_indentation.py

The script `5-text_indentation.py` provides a function `text_indentation(text)` that prints a text with two new lines after each '.', '?', and ':' characters. It raises a `TypeError` exception if the input is not a string.

### 5-text_indentation.txt

This test file contains test cases for the `text_indentation` function. It verifies that the function correctly adds new lines after specific characters and handles different text inputs.

### max_integer.py

The script `max_integer.py` includes a function `max_integer(list=[])` that finds and returns the maximum integer in a list of integers. If the list is empty, the function returns `None`.

### 6-max_integer_test.py

This test file contains unittests for the `max_integer` function. It covers various scenarios, including lists of positive and negative integers, lists with repeated values, an empty list, and a large list of integers.

## Running the Tests

To run the tests for each script, use the following command for Doctest files:

