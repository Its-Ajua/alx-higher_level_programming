#!/usr/bin/python3
"""Module containing the a class that serves as base to other classes"""


import json
import csv
import os

class Base:
    """Representation of the base of our Object Oriented Programme"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returning a json representation of the list"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json representation to the file"""
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returing the object representation"""
        if json_string is None or not json_string:
            return "[]"
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating instances from the dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_instance = (1, 2)
        elif cls is Square:
            new_instance = None
        else:
            new_instance = None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Loads strings from file"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf=8") as f:
            return [cls.create(**x) for x in cls.from_json_string(f.read())]
