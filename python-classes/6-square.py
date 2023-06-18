#!/usr/bin/python3
""" SQUARE SQUARE"""


class Square:
    """ class Square makes Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter def """
        return self.__size

    @size.setter
    def size(self, value):
        """ Square setter """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ position getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        if len(value) != 2 or\
            type(value[0]) != int or type(value[1]) != int or\
                value[0] < 0 or value[1] < 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ area of square """
        return self.__size ** 2

    def my_print(self):
        """ prints Square """
        if self.__size == 0:
            print("")
        for t in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for t in range(self.__position[0]):
                print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            print("")
