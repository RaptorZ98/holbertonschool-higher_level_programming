#!/usr/bin/python3
""" is kind of class """


def is_kind_of_class(obj, a_class):
    """ is kind of class """
    if obj is a_class:
        return True
    elif issubclass(obj, a_class):
        return True
    else:
        return False
