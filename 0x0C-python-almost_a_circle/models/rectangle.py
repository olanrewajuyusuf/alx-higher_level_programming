#!/usr/bin/python3

"""Importing Base model"""
from .base import Base 

"""Creating a Rectangle model that inherits from Base"""

class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: x axis if the rectangle
            y: y axis of the rectangle
        """

        """calling the super class with id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Creating getter and setter for y"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Creating getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Creating getter and setter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Creating getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """difining the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display method of rectangle with char #"""

        """handling position on y axis"""
        for _ in range(self.y):
            print()

        for i in range(self.__height):
            """Handling the position of # on x axis"""
            print(' ' * self.__x, end='')
            """print # rectangle"""
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """update method assigns arguments to each attribute."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """__str__ method to override the class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)
