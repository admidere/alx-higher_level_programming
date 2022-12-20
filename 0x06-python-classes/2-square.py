#!/usr/bin/python3
"""square module"""


class Square:
    """square class that contains object and
    and method inside the class"""
    def __init__(self, size=0):
        """initailized for a givem parameter
        or argument
        and encapsulat the size to protect"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
