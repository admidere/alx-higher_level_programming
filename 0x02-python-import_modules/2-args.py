#!/usr/bin/python3
import sys
if __name__ == "__main__":
    print("{} Arguments count:".format(len(sys.argv)))
    for i, arg in enumerate((sys.argv), start = 1):
        print("{}: {}".format(i, arg))
