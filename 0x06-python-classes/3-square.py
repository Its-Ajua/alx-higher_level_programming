#!/usr/bin/python3
"""Defining a square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
        size: size of the square
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates the area of the square
        Returns: the square area
        """

        return (self.__size ** 2)
