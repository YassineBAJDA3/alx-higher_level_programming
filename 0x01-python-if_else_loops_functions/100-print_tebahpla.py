#!/usr/bin/python3
for i in range(90, 64, -1):
    print("{:c}".format(i), end="") if i % 2 == 0 else print("{:c}".format(i + 32), end="")
