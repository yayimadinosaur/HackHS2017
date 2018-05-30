#!/usr/bin/python3
#by wfung

import sys
import string

def vigenere(arg1, arg2):
    key_list = list(arg1)
   # print(key_list)
    key_len = len(arg1)
    i = 0
    result = []
    if (key_len < 1):
        print("minimum key len is 1")
        exit()
    for letter in arg2:
        if letter.isalpha():
            upper = 0
            #reset key
            if i == key_len:
                i = 0
            #if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter.isupper():
                upper = -32
                #print("upped")
            result.append(((ord(letter.lower()) - ord('a') + ord(key_list[i]) - 97) % 26) + ord('a') + upper)
            i += 1
        else:
            result.append(letter)
    #print(result)
    new = []
    for e in result:
        if type(e) is int:
            new.append(chr(e))
        else:
            new.append(e)
    #print(new)
    print("".join(new))

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
