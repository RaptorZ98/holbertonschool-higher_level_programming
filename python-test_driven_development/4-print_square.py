#!/usr/bin/python3
""" print square """


def print_square(size):
    """ prints square """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for n in range(size):
            print("#", end="")
        print("")
