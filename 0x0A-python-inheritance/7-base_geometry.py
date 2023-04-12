#!/usr/bin/python3
"""module that defines a class"""


class BaseGeometry:
    """function that raises as exception if area() is not implemented"""

    def area(self):
        """method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value of an integer
        raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
