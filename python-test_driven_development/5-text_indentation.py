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
        else:
            ckeck = 0
        if letter in ['.', '!', ':']:
            print(f"{letter}\n")
            check = 1
        else:
            print(f"{letter}", end="")
