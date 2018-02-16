#!/usr/bin/python3

# Ad lib program of 4 parameters, returns song
# By wfung

import sys

y = []

def main():
    for x in range (0, 4):
        if x == 0:
            z = input('Please input an adjective: ')
        if x == 1:
            z = input('Please input an business: ')
        if x == 2:
            z = input('Please input an animal: ')
        if x == 3:
            z = input('Please input an noise: ')
        y.append(z)
    if len(sys.argv) < 2:
        i = 'Error: No Title'
    else:
        i = str(sys.argv[1])
    print('\n' + i.upper())
    print("%s Macdonald had a %s, E-I-E-I-O\n"
    "and on that %s he had a %s, E-I-E-I-O\n"
    'with a %s %s here\n'
    'and a %s %s here,\n'
    "here a %s, there a %s,\n"
    "everything a %s %s,\n%s Macdonald had a %s E-I-E-I-O!"
    % (y[0], y[1], y[1], y[2], 
        y[3], y[3], y[3], y[3], y[3], y[3], y[3], y[3], 
        y[0], y[1]))

if __name__ == "__main__":
    main()
