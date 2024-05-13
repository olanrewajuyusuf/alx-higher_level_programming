#!/usr/bin/python3

"""Importing Base model"""
from .base import Base 

"""Creating a Rectangle model that inherits from Base"""
class Rectangle(Base):

    """Creating private instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """calling the super class with id"""
        Base.__init__(self, id)

        """assigning values to private instance attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Creating getter and setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    """Creating getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    """Creating getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """Creating getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
