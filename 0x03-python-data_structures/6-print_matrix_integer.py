#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    len1 = 0
    for k in matrix:
        len1 += 1
    len2 = 0
    for d in k:
        len2 += 1
    for i in range(len1):
        for j in range(len2):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
