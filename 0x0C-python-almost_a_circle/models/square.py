#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherit from class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

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
        if args:
            if len(args) > 0:
                k = 0
                for i in args:
                    k += 1
                for j in range(k):
                    if j == 0:
                        self.id = args[0]
                    if j == 1:
                        super(Square, self.__class__).width.__set__(self, args[1])
                        super(Square, self.__class__).height.__set__(self, args[1])
                    if j == 2:
                        super(Square, self.__class__).x.__set__(self, args[2])
                    if j == 3:
                        super(Square, self.__class__).y.__set__(self, args[3])
        if kwargs:
            if len(kwargs) > 0:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    super(Square, self.__class__).width.__set__(self, kwargs["size"])
                    super(Square, self.__class__).height.__set__(self, kwargs["size"])
                if "x" in kwargs:
                    super(Square, self.__class__).x.__set__(self, kwargs["x"])
                if "y" in kwargs:
                    super(Square, self.__class__).y.__set__(self, kwargs["y"])

    def to_dictionary(self):
        """to dictionary"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
