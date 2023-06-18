#!/usr/bin/python3
""" SQUARE SQUARE"""


class Square:
    """ class Square makes Square"""

    def __init__(self, size=0):
        self.size(self, size)

    def size(self):
        """ getter def """
        return self.__size

    def size(self, value):
        """ Square setter """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area of square """
        return self.__size ** 2
