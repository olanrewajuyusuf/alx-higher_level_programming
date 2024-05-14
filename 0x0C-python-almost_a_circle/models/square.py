#!/usr/bin/python3
from models.rectangle import Rectangle

"""Creating a square model"""

class Square(Rectangle):
    """Representing square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance.

        Args:
            size: The size of the square
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return string representation of the Square instance."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)
