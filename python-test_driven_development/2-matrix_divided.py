#!/usr/bin/python3
""" matrix divided """


def matrix_divided(matrix, div):
    """ matrix matrix """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    for pos in range(len(matrix)):
        if type(matrix[pos]) != list:
            raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
        if matrix[pos + 1]:
            if len(matrix[pos]) != len(matrix[pos + 1]):
                raise TypeError("Each row of the matrix\
                                must have the same size")
        for obj in range(len(matrix[pos])):
            if type(matrix[pos][obj]) not in [int, float]:
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
    if type(div) == int or type(div) == float:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = matrix.copy()
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            newMatrix[i][n] = round(matrix[i][n] / div, 2)
    return newMatrix
