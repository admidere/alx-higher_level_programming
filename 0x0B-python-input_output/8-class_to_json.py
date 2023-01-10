#!/usr/bin/python3
"""module"""
import json


def class_to_json(obj):
    """return saved json"""
    return obj.__dict__
