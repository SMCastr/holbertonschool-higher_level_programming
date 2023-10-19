#!/usr/bin/python3

"""Module to find the max integer in a list
"""

def max_integer(my_list=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if not my_list:
        return None
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
