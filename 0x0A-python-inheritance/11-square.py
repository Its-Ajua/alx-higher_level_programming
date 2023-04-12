#!/usr/bin/python3
"""module that defines a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defining a square class"""

    def __init__(self, size):
        """initializing the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
