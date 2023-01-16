#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """class square inherit from class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size"""
        id = self.id
        x = super().x
        y = super().y
        w = super().width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, w)

    @property
    def size(self):
        """get the size value"""
        return super().width

    @size.setter
    def size(self, value):
        """set for size"""
        super(Square, self.__class__).width.__set__(self, value)
        super(Square, self.__class__).height.__set__(self, value)

    def update(self, *args, **kwargs):
        """update the value"""
        if args:
            if len(args) > 0:
                k = 0
                for i in args:
                    k += 1
                for j in range(k):
                    if j == 0:
                        self.id = args[0]
                    if j == 1:
                        super(Square, type(self)).width.__set__(self, args[1])
                        super(Square, type(self)).height.__set__(self, args[1])
                    if j == 2:
                        super(Square, type(self)).x.__set__(self, args[2])
                    if j == 3:
                        super(Square, type(self)).y.__set__(self, args[3])
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.__set__(self, kwargs["size"])
                super(Square, type(self)).height.__set__(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.__set__(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.__set__(self, kwargs["y"])

    def to_dictionary(self):
        """to dictionary"""
        id = self.id
        x = super().x
        y = super().y
        w = super().width
        return {'x': x, 'y': y, 'id': id, 'size': w}
