#!/usr/bin/python3
"""module that defines a class that inherits a list"""


class MyList(list):
    """representing a class"""

    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
