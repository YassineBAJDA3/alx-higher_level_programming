#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(string):
    for char in string:
        print("{:char}"
              .format(ord(char) if not islower(c) else ord(char) - 32),
              end="")
    print("")
