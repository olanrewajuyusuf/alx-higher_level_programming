#!/usr/bin/python 3

"""Creating a base class"""
class Base:

    """adding a private class attribute"""
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
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id =Base. __nb_objects
