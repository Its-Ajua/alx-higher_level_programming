#!/usr/bin/python3
"""module that defines a class"""


class BaseGeometry:
    """function that raises as exception if area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
