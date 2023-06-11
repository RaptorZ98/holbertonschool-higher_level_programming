#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = {}
    for element in set_1:
        for ele in set_2:
            if element == ele:
                new_set.add(element)
    return new_set
