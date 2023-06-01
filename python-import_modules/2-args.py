#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 0
    i = len(argv)
    if i == 1:
        a = "arguments."
    elif i == 2:
        a = "argument:"
    else:
        a = "arguments:"
    print("{} {}".format(i - 1, a))
    if i != 0:
        for argument in argv:
            if n != 0:
                print("{}: {}".format(n, argument))
            n += 1
