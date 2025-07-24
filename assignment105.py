'''
Create an array that has user defined inputs and with the help of for loop,
fetch all the prime numbers and print the numbers
'''

#Start of program.

mydata = list()

num = int(input("Enter number of elements into the array: "))
count = 1

while count <= num:
    element = int(input("Enter the number: " ))
    mydata.append(element)
    count += 1

print(mydata)
print("The prime numbers fetched are:")

for each in mydata:
    ct = 0
    j = 1
    while j <= each:
        if each % j == 0:
            ct += 1
        j += 1

    if ct == 2:
        print(each)

#End of program.
