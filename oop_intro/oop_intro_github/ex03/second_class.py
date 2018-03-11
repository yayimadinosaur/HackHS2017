from first_class import First_class

class Second_class(First_class):
    def __init__(self, name):
        super().hello(name)
