#!/usr/bin/python3
"""module that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """defining a rectangle"""

    def __init__(self, width, height):
        """initializing the width and height of the rectangle
        input arguments:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
