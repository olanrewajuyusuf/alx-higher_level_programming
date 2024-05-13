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
        self.__width = width

    """Creating getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    """Creating getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """Creating getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
