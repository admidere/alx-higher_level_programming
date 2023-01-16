#!/usr/bin/python3
"""class module"""
import json


class Base:
    """class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """private class attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file using json"""
        if list_objs is not None or not list_objs:
            list = []
        list = [i.to_dictionary() for i in list_objs]
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as fin:
            fin.write(cls.to_json_string(list))

    @staticmethod
    def to_json_string(list_of_dictionary):
        "return that converted to json string"
        if list_of_dictionary is None or list_of_dictionary == []:
            return json.dumps([])
        return json.dumps(list_of_dictionary)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
