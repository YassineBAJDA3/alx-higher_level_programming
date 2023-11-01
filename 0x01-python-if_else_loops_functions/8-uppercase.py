#!/usr/bin/python3
def islower(char):
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return True
    else:
        return False

def uppercase(string):
    for char in string:
        print("{:char}"
              .format(ord(char) if not islower(char) else ord(char) - 32),
              end="")
    print("")
