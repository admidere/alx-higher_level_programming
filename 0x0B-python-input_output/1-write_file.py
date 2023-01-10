#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as fin:
        return fin.write(text)
