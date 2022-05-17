# Python3 program to
# demonstrate instantiating
# a class
class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
# Driver code
# Object instantiation
r = Dog()

# Accessing class attributes
# and method through objects
print(r.attr1)
r.fun()

r1 = Dog()
print(r1.attr2)
