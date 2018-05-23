#!/usr/bin/python3
#by wfung

import sys
import string

def vigenere(arg1, arg2):
    print("a1 %s a2" % arg1, arg2)

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
