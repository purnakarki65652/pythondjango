text = "             madam          "
#remove white spaces from left and right
print(text.strip())

text="madam"
print(text.strip("m"))

text="madam"
print(text.strip("ma"))

text="mada"
print(text.strip("a"))


#count
para ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
url ="https://www.facebook.com"
url2 ="https://www.nepaltrekking.com"
print(url.count("w"))
print(url.count("w", 9, 16))
print("Found ", para.count("Lorem"), " Lorem")

print ("Welcome to {} .".format("Laba"))
print ("Welcome to Guru{} .".format("99"))
print ("Welcome to {name}{num} .".format(name="Guru", num="99"))
print ("Welcome to {0}{1} .".format("Guru","99"))
print ("{} is {} new kind of {} experience!".format("Guru99", "totally","learning"))

print("The binary to decimal value is : {:d}".format(0b0011))
print("The binary value is : {:b}".format(500))
print("The value is : {:.2f}".format(40.3455634467))
print("The value is : {:.0%}".format(0.80))
print("The value is {:_}".format(1000000))
print("The value is : {:,}".format(1000000))
print("The value is: {:5}".format(40))
print("The value is: {:-}".format(-40))
print("The value is: {:+}".format(40))
print("The value is {:=}".format(-40))

print("I have {:5} dogs and {:5} cat".format(2,1))
str1 = "Welcome to  Laba Training Center"
print("The length of the string  is :", len(str1))

center ="Laba"
print("We  are learning at %s ." %(center))


oldstring = "I Like Nepal"
newstring = oldstring.replace('like', 'love')
print(newstring)
print(newstring.upper())
print(newstring.lower())
print(",".join("Python"))
revstring=reversed(oldstring)
#print((reversed(revstring)))
string="12345"
print(''.join(reversed(oldstring)))

word="guru99 career guru99"
print(word.split(' '))

word="guru99 career guru99"
print(word.split('r'))




