#!/usr/bin/python3
"""module that defines an object of the same class"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class, otherwise false
    """
    return (type(obj) == a_class)
