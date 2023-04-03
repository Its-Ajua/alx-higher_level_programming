#!/usr/bin/python3
"""Defining a class rectangle"""


class Rectangle:
    """Representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing a rectangle
        input arguments:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting the width of the rectangle
        Raise:
        TypeError - if value is not an integer
        ValueError - if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height of the rectangle
        Raise:
        TypeError - if value is not an integer
        ValueError - if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
