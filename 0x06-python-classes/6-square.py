#!/usr/bin/python3
"""Square class module"""


class Square:
    """Represents a square defined by geometric shape
    Attributes:
        __size (int): size of square by length sides
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of square by length sides
            postion(tuple): postion of square in 2D space
        Returns: None
        """
        self.__size = size
        self.position = position

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
            print('\n'*self.__position[1], end='')
            for t in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    @property
    def position(self):
        """Get postion attribute

        Returns: The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Setter of position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
