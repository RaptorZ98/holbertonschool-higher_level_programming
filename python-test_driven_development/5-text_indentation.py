#!/usr/bin/python3
""" text indent """


def text_indentation(text):
    """ text indent """
    if type(text) != str:
        raise TypeError("text must be a string")
    check = 0
    for letter in text:
        if check == 1 and letter == " ":
            letter = ""
        elif check == 1 and letter != " ":
            ckeck = 0
            pass
        if letter in ['.', '!', ':']:
            print(f"{letter}\n")
            check = 1
        else:
            print(f"{letter}", end="")
