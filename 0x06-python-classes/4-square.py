#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initailized for a givem parameter
        or argument
        and encapsulat the size to protect"""
        self.__size = size


    @property
    def size(self):
        """size"""
        return (self.__size)


    @size.setter
    def size(self, value):
        """setter give value for old argument"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """return new area"""
        return (self.__size ** 2)
