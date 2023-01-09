#!/usr/bin/python3
"""class module"""


class BaseGeometry:
    """class area"""
    def area(self):
        """raise an error"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
