#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} argument{}{}"
        .format(len(sys.argv) - 1, "" if len(sys.argv) - 1 == 1 else "s", "." if len(sys.argv) - 1 == 0 else ":"))
    i = 1
    while i <= len(sys.argv) - 1:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
