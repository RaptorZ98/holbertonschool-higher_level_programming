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

    def area(self):
        """ area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ display the rectangle """
        for spaces in range(self.__y):
            print()
        for lines in range(self.__height):
            for jump in range(self.__x):
                print(" ", end="")
            for parts in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str str """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            size = len(args)
            if size >= 1:
                self.id = args[0]
            if size >= 2:
                self.__width = args[1]
            if size >= 3:
                self.__height = args[2]
            if size >= 4:
                self.__x = args[3]
            if size >= 5:
                self.__y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ return a dictonary """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
