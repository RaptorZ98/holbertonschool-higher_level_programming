#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_t = [0, 0]
    for i in range(min(len(tuple_a), 2)):
        new_t[i] += tuple_a[i]
    for i in range(min(len(tuple_b), 2)):
        new_t[i] += tuple_b[i]
    return tuple(new_t)
