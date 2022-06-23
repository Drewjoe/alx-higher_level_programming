#!/usr/bin/python3
"""Square class module"""


class Square:
    """Represents a square defined by geometric shape
    Attributes:
        __size (int): size of square by length sides
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of square by length sides
        Returns: None
        """
        self.__size = size
