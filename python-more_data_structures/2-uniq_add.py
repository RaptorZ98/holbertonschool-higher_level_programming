#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for pos in range(len(my_list)):
        if my_list[pos] not in my_list[:pos]:
            sum += my_list[pos]
    return sum
