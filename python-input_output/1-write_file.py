#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ writes in a file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
