#!/usr/bin/python3
""" append to file"""


def append_write(filename="", text=""):
    """ appends in a file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)