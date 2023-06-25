#!/usr/bin/python3
""" base geo """


class BaseGeometry:
    """ base geo """
    def area(self):
        """ area of """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
