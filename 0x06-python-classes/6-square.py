#!/usr/bin/python3
"""Defining a square"""


class Square:
    """Representing the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the square class
        Args:
        size: size of the square
        position: coordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """gets the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                len([i for i in value if isinstance(i, int) and i >= 0]) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square in position"""
        if self.__size == 0:
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
