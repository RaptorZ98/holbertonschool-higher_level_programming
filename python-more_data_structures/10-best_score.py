#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        res = 0
        val = [""]
        for key in a_dictionary:
            if res < a_dictionary[key]:
                res = a_dictionary[key]
                val[0] = key
        return val[0]
    else:
        return None
