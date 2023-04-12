#!/usr/bin/python3
"""module that defines a class"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """representing a class"""

    def __init__(self, width, height):
        """initializing the rectangle
        input arguments:
        width: width of the rectangle
        height: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
