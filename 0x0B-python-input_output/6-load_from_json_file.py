#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)
