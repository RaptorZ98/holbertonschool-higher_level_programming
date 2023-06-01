#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = 0
    for nums in argv:
        if n != 0:
            n += int(nums)
    print("{}".format(n))
