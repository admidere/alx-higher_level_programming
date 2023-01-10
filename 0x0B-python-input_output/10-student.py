#!/usr/bin/python3
"""class module"""


class Student:
    """class instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict"""
        if (type(attrs) == list and all(
                type(ele) == str for ele in attrs)):
            return {key: val for key, val in self.__dict__.items() if key in
                    attrs}
        return self.__dict__
