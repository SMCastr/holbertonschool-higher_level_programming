#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(num), end=" ")  # Print the number with a space at the end
            else:
                print("{:d}".format(num))  # Print the last number in the row without a space
