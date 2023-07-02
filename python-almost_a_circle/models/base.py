#!/usr/bin/python3
""" class base """
import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init of class base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dict to json """
        if list_dictionaries is None and len(list_dictionaries) != 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json string to file """
        name = f"{cls.__name__}.json"

        with open(name, 'w') as f:
            if list_objs is None:
                list = []
            else:
                list = []
                for obj in list_objs:
                    list.append(obj.to_dictionary())
            f.write(cls.to_json_string(list))
