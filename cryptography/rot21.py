#!/usr/bin/python3

import sys
import string

def rot21(arg1):
    i = 0
    x = list(arg1)
    while i < len(arg1):
        if arg1[i].isalpha():
            result = ord(arg1[i])
            if 69 >= result >= 65:
                result += 21
            elif 90 >= result >= 70:
                result -= 5
            elif 101 >= result >= 97:
                result += 21
            elif 122 >= result >= 102:
                result -= 5
            x[i] = chr(result)
        i += 1
    return (''.join(x))

if __name__ == "__main__":
    if len(sys.argv) - 1 != 1:
        print("program only takes 1 arg")
        exit()
    result = rot21(sys.argv[1])
    print(result)
