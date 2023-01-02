#!/usr/bin/python3
"""class module"""


class Rectangle:
    """class module"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        """ return private height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """set value for what we want to do"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
