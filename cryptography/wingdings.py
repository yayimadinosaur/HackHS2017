#!/usr/bin/python3
#by wfung

import sys
import string

#converts alpha to emoji based on ascii value
def convert_alpha(alpha_char):
    upper_check = 0
    emoji_list = ['\U0001F600',
            '\U0001F601',
            '\U0001F602',
            '\U0001F603',
            '\U0001F604',
            '\U0001F605',
            '\U0001F606',
            '\U0001F607',
            '\U0001F608',
            '\U0001F609',
            '\U0001F610',
            '\U0001F611',
            '\U0001F612',
            '\U0001F613',
            '\U0001F614',
            '\U0001F615',
            '\U0001F616',
            '\U0001F617',
            '\U0001F618',
            '\U0001F619',
            '\U0001F620',
            '\U0001F621',
            '\U0001F622',
            '\U0001F623',
            '\U0001F624',
            '\U0001F625']
    alpha_char = alpha_char.lower()
    alpha_char = ord(alpha_char)
    alpha_char -= 97
    return emoji_list[alpha_char]

#if character is an alphabet char, pass into convert_alpha function
def wingdings(arg1):
    x = list(arg1)
    wingdinged_str = []
    for letter in x:
        if letter.isalpha():
            letter = convert_alpha(letter)
        wingdinged_str.append(letter)
    return(wingdinged_str)

def main():
    if len(sys.argv) - 1 != 1:
        print("program only takes 1 arg")
        exit()
    result = wingdings(sys.argv[1])
    result = ''.join(result)
    print(result)

if __name__ == "__main__":
    main()
