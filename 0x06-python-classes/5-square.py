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
        self.__size = size

    def area(self):
        """Calculates the square area
        Returns: area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size
        Args:
            value (int): size of the side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns: None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square using the character #

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        else:
            for t in range(self.__size):
                print("#" * self.__size)
