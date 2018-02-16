#!/usr/bin/env python3
#By wfung

#program contains secret 5 letter word and gives clues with 10 max guesses

import sys
import random
import string

#made a word bank for each letter since pdf doesn't specify
word_bank = ["apple",
        "bread",
        "candy",
        "donut",
        "eagle",
        "fruit",
        "grape",
        "horse",
        "icing",
        "jelly",
        "kabob",
        "llama",
        "mango",
        "nacho",
        "onion",
        "pasta",
        "quail",
        "raven",
        "skunk",
        "toast",
        "unity",
        "valid",
        "while",
        "xerox",
        "yahoo",
        "zebra"]

#generate random alphabet letter
def random_letter():
    return random.choice(string.ascii_uppercase) 

def main():
    y = random_letter()
    index = ord(y) - 65
    word = word_bank[index]

    for i in range(0, 10):
        if i == 0:
            x = input("The secret word begins with a %c.\n" % y)
            y = y.lower()
        else:
            x = input("GUESS:")
        if x == '':
            print("You wasted a guess =P")
        if len(x) > 5 or len(x) < 5:
            print("0, 1, 2, 3, 4 that's how we count to five!")
        if len(x) == 5:
            if x[0] != y.lower():
                print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            else:
                if x == word:
                    print("Good Job! You are one with the Source.")
                    exit()
                else:
                    guess = 9 - i
                    if guess == 0:
                        exit()
                    print("You have %d guesses left!" % (guess))
    exit()

if __name__ == "__main__":
    main()
