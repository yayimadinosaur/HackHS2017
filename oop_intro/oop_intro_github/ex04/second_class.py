import random
from first_class import First_class

class Second_class(First_class):
    def __init__(self, name):
        super().hello(name, Second_class.number())
    def number():
        print("Number Method in Second_Class is called")
        return (random.randrange(1, 7))
