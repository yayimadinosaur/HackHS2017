import random
from first_class import First_class

class Second_class(First_class):
    def __init__(self, name, hobby):
        super().hello(name, Second_class.number())
        self.hobby = hobby
    def number():
        print("Number Method in Second_Class is called")
        return (random.randrange(1, 7))
    def getHobby(self):
        return self.hobby
