#!/usr/bin/python3
""" class base """


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init of class base """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
