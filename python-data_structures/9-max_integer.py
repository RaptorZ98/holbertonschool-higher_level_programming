#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = my_list[0]
        for i in range(len(my_list)):
            if i > x:
                x = i
        return x
    else:
        return None
