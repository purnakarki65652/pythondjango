print ("Hello, Python!")
print("HI")

if True:
    print ("Answer \n True")

else:
    print ("Answer \n True")
print("I am outside of the block")
#Multi-Line Statements
#continuation character (\)
total = "item_one + \
                item_two + \
    item_three"
print (total)

# Quotations
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
#This is an example of multiline Comments
# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
#multiline Comments
'''
This is a multiline
comment.
'''
#Multiple Statements on a Single Line
import sys
x= 'foo'
sys.stdout.write(x + '\n ')
# is equal to
import sys; x = 'foo'; sys.stdout.write(x + '\n')

#variables declaration
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter," " , miles, " ", name);

#multiple assignment
a=b=c=1;
name,address,gender = "Dharma" ,"Kathmandu", "Male"

#data types
    #Numbers
    #String
    #List
    #Tuple
    #Dictionary
#Numbers
  # int (signed integers)
# long (long integers, they can also be represented in octal and hexadecimal)
# float (floating point real values)
# complex (complex numbers)

#Strings
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5] )    # Prints characters starting from 3rd to 5th
print (str[2:] )     # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[-5:])