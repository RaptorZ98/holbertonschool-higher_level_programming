#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        res = 0
        for num in a_dictionary.values():
            if res < num:
                res = num
        return res
    else:
        return None
