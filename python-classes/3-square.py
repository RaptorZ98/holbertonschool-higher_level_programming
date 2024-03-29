#!/usr/bin/python3
""" SQUARE SQUARE"""


class Square:
    """ class Square makes Square"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area of square """
        return self.__size ** 2
