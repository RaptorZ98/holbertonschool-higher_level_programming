#!/usr/bin/python3
""" text indent """


def text_indentation(text):
    """ text indent """
    if type(text) != str:
        raise TypeError("text must be a string")
    check = 0
    for letter in text:
        if check == 1 and letter == ' ':
            letter = ""
        else:
            check = 0
        if letter in ['.', '?', ':']:
            check = 1
            print(f"{letter}\n")
        else:
            print(letter, end="")  
