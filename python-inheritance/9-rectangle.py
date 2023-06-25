#!/usr/bin/python3
""" base geo """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle rect """
    def __init__(self, width, height):
        """ init init """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """ str str """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ area area """
        return self.__height * self.__width
