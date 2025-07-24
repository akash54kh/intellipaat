'''
Write a function that takes 2 arrays and prints the members of the first
array that are present in the second array.
'''

#Beginning of the Program

x = input("Enter the number of elements into the 1st arrray: ")
x = int(x)

mydata1 = list()

count = 1
print("Enter the numbers into this array.")

while count <= x:
    element = int(input("Enter the number: " ))
    mydata1.append(element)
    count += 1

y = input("Enter the number of elements into the 2nd arrray: ")
y = int(y)

mydata2 = list()

count = 1
print("Enter the numbers into this array.")

while count <= y:
    element = int(input("Enter the number: " ))
    mydata2.append(element)
    count += 1

mydata3 = list()

for each in mydata1:
    if each in mydata2:
        mydata3.append(each)

print("The resultant list is as follows:")
print(mydata3)

# End of the program.
