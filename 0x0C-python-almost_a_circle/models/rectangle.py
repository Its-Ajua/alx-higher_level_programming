#!/usr/bin/python3
"""Module for our rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representing a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieving width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of the width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieving height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieving x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value of the x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """retrieving y of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """setting the value of the y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """retrieving the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using #"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """format for the string representation of the class"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates instance attributes"""
        if args and len(args) != 0:
            x = 0
            for i in args:
                if x == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif x == 1:
                    self.width = i
                elif x == 2:
                    self.height = i
                elif x == 3:
                    self.x = i
                elif x == 4:
                    self.y = i

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif a == width:
                    self.width = b
                elif a == height:
                    self.height = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """Returns dictionary representation of the class"""
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}
