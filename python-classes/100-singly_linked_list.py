#!/usr/bin/python3

class Node:
    """
    Class Node defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Class SinglyLinkedList defines a singly linked list.

    Attributes:
        head: The head of the linked list.
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

# Test the SinglyLinkedList class
if __name__ == "__main__":
    # Additional test cases
    n1 = Node(3)
    n2 = Node(-5)
    n3 = Node(4)
    n3.next_node = n2

    try:
        n4 = Node("4")
    except Exception as e:
        print(e)

    try:
        n2.next_node = "Node"
    except Exception as e:
        print(e)

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    print(sll)

    sll = SinglyLinkedList()
    sll.sorted_insert(1)
    sll.sorted_insert(2)
    sll.sorted_insert(3)
    sll.sorted_insert(4)
    print(sll)

    sll = SinglyLinkedList()
    sll.sorted_insert(1)
    sll.sorted_insert(2)
    sll.sorted_insert(3)
    sll.sorted_insert(4)
    sll.sorted_insert(4)
    sll.sorted_insert(3)
    sll.sorted_insert(2)
    sll.sorted_insert(1)
    print(sll)

    sll = SinglyLinkedList()
    sll.sorted_insert(10)
    sll.sorted_insert(2)
    sll.sorted_insert(-3)
    sll.sorted_insert(34)
    sll.sorted_insert(4)
    sll.sorted_insert(-5)
    sll.sorted_insert(0)
    sll.sorted_insert(8)
    sll.sorted_insert(7)
    print(sll)

    sll = SinglyLinkedList()
    print(sll)
