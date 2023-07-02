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
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if isinstance(value, int):
            if value > 0:
                self.width = value
                self.height = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            size = len(args)
            if size >= 1:
                self.id = args[0]
            if size >= 2:
                self.size = args[1]
            if size >= 3:
                self.x = args[2]
            if size >= 4:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
