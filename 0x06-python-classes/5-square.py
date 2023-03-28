#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square class"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
        size: represents the size of the square
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
        """Retrieves the size of square"""
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
        Returns: The square area
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in stdout with character # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
