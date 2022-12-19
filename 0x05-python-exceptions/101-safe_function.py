#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
