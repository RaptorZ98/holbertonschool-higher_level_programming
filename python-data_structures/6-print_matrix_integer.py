#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        t = 0
        for x in matrix:
            for num in x:
                if t == 1:
                    print(" ", end="")
                print("{:d}".format(num), end="")
                t = 1
            t = 0
            print("")
    else:
        print("")
