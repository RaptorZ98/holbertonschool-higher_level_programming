#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number %= -10
        print("{}".format(number))
        return number
    number % 10
    print("{}".format(number))
    return number