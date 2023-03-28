#!/usr/bin/python3
"""Defining a square """


class Square:
    """Representing a square class"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
        size: size of the square
        Raises:
        TypeError: if size is not integer
        ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns: the square area
        """

        return (self.__size ** 2)
