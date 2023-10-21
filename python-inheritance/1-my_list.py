#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """
        Print the list sorted in ascending order.

        Attributes:
            self: The object itself.

        Returns:
            None.
        """
        print(sorted(self))
