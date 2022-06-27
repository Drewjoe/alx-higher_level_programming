#!/usr/bin/python3
""" Singly linked list module
"""


class Node():
    """Represents a node in a singly linked list

    Attributes:
        data (int): data stored inside the node
        next_node (Node): next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """ Instantializes the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter of the attribute data

        Returns:
            The stored data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter of the attribure data

        Args:
            value (int): the given data
        Raises:
            TypeError: if value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter of the next_node

        Returns:
            A pointer to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter of the next_node

        Args:
            value (Node): next node in the linked list
        Raises:
            TypeError: if value not node or None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """ Represents a single linked list

    Attributes:
        head (Node): head of the linked list
    """

    def __init__(self):
        """ Class initializer

        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node instance into the correct sorted position

        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ String representation of SinglyLinkedList instance

        Returns:
            Formatted string representing the linked list
        """
        result = ""
        tmp = self.__head
        while tmp is not None:
            result += str(tmp)
            if tmp.next_node is not None:
                result += '\n'
            tmp = tmp.next_node
        return result
