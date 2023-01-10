#!/usr/bin/python3
"""module"""
import json


def save_to_json_file(my_obj, filename):
    """print json file added"""
    with open(filename, "w", encoding="utf-8") as fin:
        json.dump(my_obj, fin)
