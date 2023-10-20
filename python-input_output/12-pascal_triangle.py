#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        last_row = triangle[-1]
        new_row = [1]  # First element in a row is always 1

        for i in range(1, len(last_row)):
            new_element = last_row[i - 1] + last_row[i]
            new_row.append(new_element)

        new_row.append(1)  # Last element in a row is always 1
        triangle.append(new_row)

    return triangle
