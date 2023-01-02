#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """retrun the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    print_symbol = "#"

    def __str__(self):
        """return string"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)
                if i != self.__height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        """return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return Rectangle(size, size)
