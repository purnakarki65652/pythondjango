import Functions
import math as m
from Functions import sum1,  absolute_value
from Functions import *
from math import *
#Python import statement
#Import with renaming
#Python from...import statement
# import all names from the standard module Functions
# import all names from the standard module math
print(sum1(12,12))
total = Functions.sum(10,20)
print("Sum = ", total)
sqr = m.sqrt(4)
pi = m.pi;
print(pi)
print(sqr)

name = input("Enter your Name? ")
#function Call
Functions.greet(name)