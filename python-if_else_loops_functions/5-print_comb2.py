#!/usr/bin/python3
for i in range(0, 100):
    if i > 0:
        print(" ,", end="")
    print("{}{}".format(i // 10, i % 10), end="")
print("")