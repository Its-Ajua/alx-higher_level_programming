#!/usr/bin/python3
"""module that defines a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """defining a square class"""

    def __init__(self, size):
        """initializing the square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implementing area method"""
        return (self.__size ** 2)
