#!/usr/bin/python3
#by wfung

import sys
import string

def vigenere(arg1, arg2):
    key_list = list(arg1)
    print(key_list)
    key_len = len(arg1)
    i = 0
    result = []
    for letter in arg2:
        print("letter %c" % letter)
        if letter.isalpha():
            upper = 0
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                upper = 1
            print("letter %c %i keylist %c %i" % (letter, ord(letter), key_list[i], ord(key_list[i])))
            #pew = ord(letter) - 97 + ord(key_list[i]) - 97
            index = ord(letter) - 97
            move = ord(key_list[i]) - 97
            print("move = %i" % move)
            print("index = %i" % index)
            pew = index + move
            if pew > 26:
                pew %= 26
            result.append(ord(letter) + pew)
            i += 1
        else:
            print("else %c" % letter)
            result.append(letter)
        print("%s i = %i" % (result, i))
        if i > key_len:
            i = 0
    print(result)

def main():
    arg_len = len(sys.argv) - 1
    if arg_len == 1: 
        print("missing secret message in arg2")
    elif arg_len > 2:
        print("too many args")
    elif arg_len == 0:
        print("program takes 2 args: \"key\" \"secretmessage\"")
    else:
        vigenere(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
