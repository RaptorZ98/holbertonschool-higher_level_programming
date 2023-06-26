#!/usr/bin/python3
""" student student """


class Student:
    """ student student """
    def __init__(self, first_name, last_name, age):
        """ init init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            new_dic = {}
            i = 0
            for att in self.__dict__:
                if att in attrs:
                    new_dic[att] = self.__dict__.get(att)
                    i += 1
            return new_dic
        else:
            return self.__dict__
