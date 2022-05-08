#The append() method appends an element to the end of the list.
#Syntax: list.append(elmnt)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#The clear() method removes all the elements from a list.
#Remove all elements from the fruits list:
#Syntax: list.clear()
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#The copy() method returns a copy of the specified list.
#Copy the fruits list:
#Syntax: list.copy()
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#The count() method returns the number of elements with the specified value.
#Syntax: list.count(value)
#Return the number of times the value "cherry" appears in the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
y=len(fruits)
print(x)
print(f"Total length of Fruits array is {y} ")

#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
#Syntax: list.extend(iterable)
#Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#The index() method returns the position at the first occurrence of the specified value.
# Syntax: list.index(elmnt)
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#The insert() method inserts the specified value at the specified position.
#Syntax list.insert(pos, elmnt)
#pos: Required. A number specifying in which position to insert the value
#elmnt : Required. An element of any type (string, number, object etc.)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#The reverse() method reverses the sorting order of the elements.
#Syntax: list.reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


#The sort() method sorts the list ascending by default.
#You can also make a function to decide the sorting criteria(s).
#Syntax: list.sort(reverse=True|False, key=myFunc)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)




# Write a program to ask the numbers of users
# add the names by user input
# ask the user to search any names
# if found give result "Search {realName} Found"
number = int(input("How many names you want to add: "))
names=[]
for i in range(number):
    name = input("Enter the Name: ")
    names.append(name)
print(names)
search =input("Enter the name for Search: ")
count = names.count(search)
if count>=1:
    print(f"Search {search } Found")
else:
    print(f"Search {search } Not Found")


