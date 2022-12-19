#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as i:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
