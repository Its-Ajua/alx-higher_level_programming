#!/usr/bin/python3
"""Defining the rectangle class"""


class Rectangle:
    """Representing a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        input arguments:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returning the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the value of the width of the rectangle
        Raise:
        TypeError - if width is not an integer
        ValueError - if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returning the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting the value of the height of the rectangle
        Raise:
        TypeError - if height is not an integer
        ValueError - if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
