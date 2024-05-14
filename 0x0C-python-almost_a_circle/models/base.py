#!/usr/bin/python3
import json

"""Creating a base model"""

class Base:
    """adding a private class attribute

    Attrributes:
        __nb_objects (int): the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        checking if id is not none

        assign the public instance id with
        the argument value

        otherwise, increment the __nb_objects

        and assign the value to the public instance
        attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation

        args:
            list_dictionaries: dict to turn to json
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
