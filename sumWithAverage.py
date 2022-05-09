#Sum with Average example with userinput
number = int(input("How many numbers you want to add: "))
sum = 0;
average =0
for i in range(number):
    num = int(input(f"Enter the number {i+1} : "))
    sum=sum+num
average = float(sum/number)
print(f"The Sum is {sum}")
print(f"The Average is  {average}")

# Find the greatest Number
# Find the Smallest NumberS
