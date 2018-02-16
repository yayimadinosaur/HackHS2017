#!/usr/bin/env python3

#program asks if you're the mother of dragons
#By wfung

import sys

def main():
    x = input("Who goes there?\n")
    if (x == 'DHTFHNUQARFMQMKGSPRLRSKBCMD'
            or x == "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons"):
        print("Welcome, Daenerys.")
    elif x == 'Dany':
        print("Dany who?")
    else:
        print("Move along, now.")

if __name__ == "__main__":
    main()
