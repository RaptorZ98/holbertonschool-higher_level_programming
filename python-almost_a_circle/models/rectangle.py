#!/usr/bin/python3
""" class rectangle """
from models.base import Base


class Rectangle(Base):
    """ class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def display(self):
        """ display the rectangle """
        for lines in range(self.__height):
            for parts in range(self.__width):
                print("#", end="")
            print

    def __str__(self):
        return f"[Rectangle] ({Base.id}) {self.__x}/{self.__y}\
            - {self.__width}/{self.__height}"
