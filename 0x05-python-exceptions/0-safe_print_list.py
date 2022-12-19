#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            j += 1
        except Exception:
            pass
    print()
    return (j)
