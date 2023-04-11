#!/usr/bin/python3
"""module that defines a class"""


class BaseGeometry:
    """function that raises as exception if area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value os an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
