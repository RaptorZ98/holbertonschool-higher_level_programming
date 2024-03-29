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
        if list_dictionaries is None or not list_dictionaries:
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

    @staticmethod
    def from_json_string(json_string):
        """ from json to string """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create instance """
        if cls.__name__ == "Square":
            instance = cls(1)
        elif cls.__name__ == "Rectangle":
            instance = cls(1, 2)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ load from a file """
        name = f"{cls.__name__}.json"
        try:
            with open(name, 'r') as f:
                list = []
                Olist = cls.from_json_string(f.read())
                for obj in Olist:
                    list.append(cls.create(**obj))
                return list
        except Exception:
            return []
