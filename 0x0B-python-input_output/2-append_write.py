#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """open file for append to file"""
    with open(filename, "a", encoding="utf-8") as fin:
        return fin.write(text)
