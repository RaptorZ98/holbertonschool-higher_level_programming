#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divs = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divs.append(True)
        else:
            divs.append(False)
    return divs
