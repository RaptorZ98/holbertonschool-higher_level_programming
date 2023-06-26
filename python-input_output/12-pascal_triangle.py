#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        row = [1]
        for m in range(len(triangle) - 1):
            row.append(triangle[i][m] + triangle[i][m + 1])
        row.append(1)
        triangle.append(row)
    return triangle
