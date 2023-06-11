#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = dict()
    for key in a_dictionary:
        new_d.update({key: a_dictionary[key] * 2})
    return new_d
