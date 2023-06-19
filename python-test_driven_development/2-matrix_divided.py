#!/usr/bin/python3
""" matrix divided """


def matrix_divided(matrix, div):
    """ matrix matrix """

    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(err)
    for pos in range(len(matrix)):
        if type(matrix[pos]) != list:
            raise TypeError(err)
        if pos != len(matrix) - 1:
            if len(matrix[pos]) != len(matrix[pos + 1]):
                raise TypeError(err2)
        for i in range(len(matrix[pos])):
            if type(matrix[pos][i]) not in [int, float]:
                raise TypeError(err)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = matrix.copy()
    for n in range(len(matrix)):
        newMatrix[n] = list(map(lambda x: round(x / div, 2), matrix[n]))
    return newMatrix
