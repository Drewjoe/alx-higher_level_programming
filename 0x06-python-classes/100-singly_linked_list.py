#!/usr/bin/python3
"""
Singly linked list Module
"""


class Node:
    """
    Node class
    Attributes:
        data (int): the data stored in the node
        next_node (Node): a pointer to the next node
            in the linked list
    """
    def __init__(self, data, next_node=None):
        """
        Class initializer
        Args:
            data (int): the data stored in the node.
            next_node (Node): a pointer to the next node
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """
        Getter of the attribute data
        Returns:
            data: the stored data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter of the attribure data
        Args:
            value (int): the given data
        Raises:
            TypeError: if value is not integer
        """
        if type(value) is not int:
            raise TypeError("data must be integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter of the __next_node
        Returns:
            next_node: a pointer to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter of the next_node
        Args:
            value (Node): a pointer to the next node
        Raises:
            TypeError: if value not node or None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")

    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """
    SiglyLinkedList defines the singly linked list
    Attributes:
        head (Node): a pointer to the singly linked list
    """
    def __init__(self):
        """
        Class initializer
        """
        self.__head = None

    def __str__(self):
        """String representation of SinglyLinkedList instance
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string

    def sorted_insert(self, value):
        """
        Inserts new Node into the correct sorted position
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
