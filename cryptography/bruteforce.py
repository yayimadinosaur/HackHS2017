#!/usr/bin/python3

#made by wfung

import sys

#rots char i times
def rot(char, i):
    upper_check = 0
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper_check = 1
    char = char.lower()
    char = ord(char)
    char -= 97
    char += i
    char = char % 26
    char += 97
    if upper_check == 1:
        char -= 32
    return chr(char)

#passes arg1 into rot 26 times, for each letter in a-z
def main():
    x = list(sys.argv[1])
    i = 1
    while i < 27:
        new_list = []
        for letter in x:
            if letter.isalpha():
                letter = rot(letter, i)
            new_list.append(letter)
        i += 1
        rot_string = ''.join(new_list)
        print(rot_string)

if __name__ == "__main__":
    if len(sys.argv) - 1 != 1:
        print("program only takes 1 arg") 
        exit()
    main()
