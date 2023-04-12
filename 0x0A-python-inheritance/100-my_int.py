#!/usr/bin/python3
"""module that defines a class"""


class MyInt(int):
    """defining a class"""

    def __eq__(self, other):
        """Overrides equals, inverting it"""
        return (int(self) != int(other))

    def __ne__(self, other):
        """Overrides not-equals, inverting it"""
        return (int(self) == int(other))
