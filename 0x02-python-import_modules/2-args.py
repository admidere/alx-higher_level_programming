#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(index, "" if index == 1 else "s", "." if index == 0 else ":"))
    i = 1
    while i <= index:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
