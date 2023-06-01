#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 0
    i = 0
    for nums in argv:
        if i != 0:
            n += int(nums)
        i = 1
    print("{}".format(n))
