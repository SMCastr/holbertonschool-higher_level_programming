#!/usr/bin/python3

class MyList(list):
    """ Class that inherits from list. """
    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        sorted = []
        for i in self:
            sorted.append(i)
        sorted.sort()
        print(sorted)
