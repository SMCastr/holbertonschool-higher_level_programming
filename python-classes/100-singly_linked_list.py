#!/usr/bin/python3

class Node:
    """
    Class Node defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next_node attribute.

        Returns:
            Node: The reference to the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class SinglyLinkedList defines a singly linked list.

    Attributes:
        __head: The head of the linked list.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


    def __str__(self):
        """
        Custom __str__ method to print the entire list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()