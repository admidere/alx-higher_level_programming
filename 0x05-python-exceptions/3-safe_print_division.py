#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = a / b
    except Exception:
        x = None
    finally:
        print("Inside result: {}".format(x), end="\n")
        return(x)
    print()
