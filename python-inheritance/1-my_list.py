#!/usr/bin/python3

class MyList(list):
    """
    MyList is a subclass of the built-in 'list' class. It inherits all the functionality of the list class.

    Public Methods:
        print_sorted(self): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)  # Print the unsorted list
    my_list.print_sorted()  # Print the sorted list
    print(my_list)  # Print the original unsorted list again
