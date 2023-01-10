#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """file open for read"""
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        print(f.read())
