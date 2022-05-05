#Array
import array
balance = array.array('i', [300,200,100,23,23,45,56,68,98,67,56,78,56])
#print last index
print("Array last element is:", balance[-1])
#print 1st index
print(balance[1])
#print Array
print(balance)
#print all datas
for i in balance:
    print(i, end = " ")
#accessing by :
#This operation is called a slicing operation.
print(balance[:])
print(balance[1:4])

#Insert array elements
balance.insert(2, 150)
print(balance[:])

#modify array elements
balance[0]=100
print(balance[:])

#We can also perform concatenation operations on arrays in Python.
#Example:
first = array.array('b', [4, 6, 8])
second = array.array('b', [6, 12, 15])
numbers = array.array('b')
numbers = first + second
print(numbers)
#print concatenatied array
for i in numbers:
    print(i)
#removing items from an array
first.pop(2)
print(first)
#del also used to delete the items
del first[1]
print(first)


#remove array items by value
numbers.remove(6)
print(numbers)
print("The length of the array is ", len(numbers))







#names = array.array('u', ["Mukesh", "Sabin" , "Mina", "Chandan" , "Nabin", "Purna"])
#print(names[3])
