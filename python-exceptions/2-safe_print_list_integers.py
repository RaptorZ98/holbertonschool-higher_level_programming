#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    res = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except IndexError:
            break
        except ValueError:
            continue
    print("")
    return res
