#!/usr/bin/python3
""" inherits from """


def inherits_from(obj, a_class):
    """ inherits from """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
