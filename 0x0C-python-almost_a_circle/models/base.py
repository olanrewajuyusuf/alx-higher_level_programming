#!/usr/bin/python3
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
