#!/usr/bin/python3
from models.rectangle import Rectangle

"""Craeting Square model"""

class Square(Rectangle):
    """Representing square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing square instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """setter and getter method of size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returning str representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
