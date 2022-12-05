#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for j in i:
            if j == i[-1]:
                A = ""
            else:
                A = " "
            print("{:d}".format(j), end = A)
        print()
