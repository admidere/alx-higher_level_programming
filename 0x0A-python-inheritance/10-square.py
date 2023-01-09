#!/usr/bin/python3
"""class module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class inherit from class rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
