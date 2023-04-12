#!/usr/bin/python3
"""module that adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object
    input arguments:
    obj: object to which the new attribute is to be added
    attr: new attribute to be added
    value: attribute value
    Raises:
    TpyeError: if object cannot have anew attribute
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
