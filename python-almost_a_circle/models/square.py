#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init for class square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str of the square """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}"
