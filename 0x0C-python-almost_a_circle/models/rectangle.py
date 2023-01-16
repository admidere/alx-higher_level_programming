#!/usr/bin/python3
"""class module"""
from models.base import Base
import json


class Rectangle(Base):
    """class attribute"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value for hieght if it is an int"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value for an x if it is int"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set value for y if it is an int and greater than 0"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectnagle"""
        return self.__width * self.__height

    def display(self):
        """display # with given width and height
        we don't need control what a given value
        of x and y"""
        if self.__width == 0 and self.__height == 0:
            print("")

        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print('#', end="")for j in range(self.__width)]
            print()

    def __str__(self):
        """string overriding"""
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """use args and kwargs for passing the
        number of arguments"""
        if args:
            k = 0
            for j in args:
                k += 1
            if len(args) > 0:
                for i in range(k):
                    if i == 0:
                        self.id = args[0]
                    if i == 1:
                        self.__width = args[1]
                    if i == 2:
                        self.__height = args[2]
                    if i == 3:
                        self.__x = args[3]
                    if i == 4:
                        self.__y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """convert to dictionary for a given value"""
        return {"y": self.__y, "x": self.__x, "id": self.id,
                 "width": self.__width, "height": self.__height}
