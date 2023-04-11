#!/usr/bin/python3
"""module that returns a specific kind of class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if object is an instance of,
    or if the object is an instance of a class; otherwise False
    """
    return (isinstance(obj, a_class))
