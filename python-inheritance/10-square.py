#!/usr/bin/python3
""" square square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ rect rect """
    def __init__(self, size):
        """ init init """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """ area area """
        return self.__size * self.__size

    def __str__(self):
        """ init init """
        return f"[Square] {self.__size}/{self.__size}"
