#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) - 1 == 0:
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
