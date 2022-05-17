# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'
    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color
    # Objects of Dog class

