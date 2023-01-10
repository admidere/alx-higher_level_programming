#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """file open for write"""
    with open(filename, "w", encoding="utf-8") as fin:
        try:
            return fin.write(text)
        except Exception:
            return False
