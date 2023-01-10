#!/usr/bin/python3
"""module"""
import json


MyClass = __import__('8-my_class').MyClass
def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)
