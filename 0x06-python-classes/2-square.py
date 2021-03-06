#!/usr/bin/python3
"""Square class module"""


class Square:
    """Represents a square defined by geometric shape

    Attributes:
        __size (int): size of square by length sides
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of square by length sides

        Returns: None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
