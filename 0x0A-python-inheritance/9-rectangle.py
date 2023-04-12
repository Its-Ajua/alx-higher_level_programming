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

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """method should be implemented"""
        return (self.__width * self.__height)

    return ("[{}] {}/{}".format(type(self).__name__, self.__width, self.__height))
