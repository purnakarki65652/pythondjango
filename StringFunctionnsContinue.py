mystring = "Meet Guru99 Past Site.Best site for Python "
print("The position of s is at:", mystring.find("z"))

print("The position of s is at:", mystring.find("s", 20))

print("The position of s is at:", mystring.find("Python", 5))

#rfind()
#index()

my_string = "test string test, test string testing, test string test string"
startIndex = 0
count = 0
for i in range(len(my_string)):
    k = my_string.find('test', startIndex)
    if(k != -1):
        startIndex = k+1
        count += 1
        k = 0
print("The total count of substring test is: ", count )

text = "Hello World Guru99"
# splits at space
print(text.split())
text = "Hello,World, Guru99"
# splits at ','
print(text.split(", "))
text = "Hello,World:, Guru99 is one of the site:  for learning different applications"
# Splits at ':'
print(text.split(":"))

text='Hello, World, Guru99, test, testing is not done yet'
split_1 = text.split(',',2)
print(split_1)
text='Hello World Guru99'
split_1 = text.split(',',4)
print(split_1)

