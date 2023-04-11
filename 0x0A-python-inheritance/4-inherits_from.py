#!/usr/bin/python3
"""module that defines an object that is inherited from a specific class"""


def inherits_from(obj, a_class):
    """function that returns True if object is an instance;
    otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
