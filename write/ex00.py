#!/usr/bin/env python3

#program does 3 tasks
#   first, every other letter is capitalized
#   second, every capitalized vowel is replaced by a *
#   third, checks if each '(' has a matching ')'
# By wfung

import sys

def main():
    count = 0
    if len(sys.argv) != 2:
        print("Incorrect # of arguments\n")
        return ()
    line1 = str(sys.argv[1])
    line1_new = ""
    line2 = ""
    for i, c in enumerate(line1):
        if c.isalpha():
            if count == 0:
                line1_new += c.upper()
                if c.upper() in 'AEIOU':
                    line2 += '*'
                else:
                    line2 += c
                count += 1
            else:
                line1_new += c
                line2 += c
                count -= 1
        else:
            line1_new += c
            line2 += c
    print(line1_new)
    print(line2)

if __name__ == "__main__":
    main()
