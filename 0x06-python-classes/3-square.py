#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initailized for a givem parameter
        or argument
        and encapsulat the size to protect"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
        