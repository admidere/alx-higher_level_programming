#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """file open for read"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
