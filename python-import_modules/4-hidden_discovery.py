#!/usr/bin/python3
import hidden_4.pyc
if __name__ == "__main__":
    for names in hidden_4:
        if names[0] != "_":
            print("{}".format(names))
