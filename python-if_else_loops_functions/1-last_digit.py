#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number}", end="")
if number < 0:
    number = number % -10
else:
    number = number % 10
if number > 5:
    print(f" is {number} and is greater than 5")
elif number == 0:
    print(f" is 0 and is 0")
else:
    print(f" is {number} and is less than 6 and not 0")
