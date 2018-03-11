#!/usr/bin/python3

from second_class import Second_class

if __name__ == "__main__":
    name = "wfung"
    #Second_class.number()
    x = Second_class(name, "lazy")
    print("Your hobby is being %s" % (Second_class.getHobby(x)))
