#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number % -10
        print("{}".format(number * -1), end="")
        return number * -1
    number %= 10
    print("{}".format(number), end="")
    return number
