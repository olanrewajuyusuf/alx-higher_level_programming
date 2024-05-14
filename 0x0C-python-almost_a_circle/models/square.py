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

    def update(self, *args, **kwargs):
        """Assign positional and keyword arguments to attributes."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of a Square"""
        dict = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dict

    def __str__(self):
        """Returning str representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
