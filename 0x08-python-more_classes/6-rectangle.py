#!/usr/bin/python3
"""Defining the rectangle class"""


class Rectangle:
    """representing the rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        Input Arguments:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returning the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting the value of the width of the rectangle
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
        """returning the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the value of the height of the rectangle
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
        """returning the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returning the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Diagram of the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
                if i < (self.__height - 1):
                    rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns a string representation of a rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints the message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
