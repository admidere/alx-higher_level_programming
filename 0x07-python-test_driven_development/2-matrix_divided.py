#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row , list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    #return ([[round(element / div, 2) for element in row] for row in matrix])
    new_matrix = []
    for row in range(len(matrix)):
        matrix_row = []
        for col in range(len(matrix[row])):
            matrix_row.append(round(matrix[row][col] / div, 2))
        new_matrix.append(matrix_row)
    return new_matrix
