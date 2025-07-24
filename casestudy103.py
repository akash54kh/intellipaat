'''
Write a function to take an array and return another array that contains the
members of the first array that are even.
'''

#Start of Program:

x = input("Enter the number of elements into the arrray: ")
x = int(x)

mydata = list()

count = 1
print("Enter the numbers into the array.")

while count <= x:
    element = int(input("Enter the number: " ))
    mydata.append(element)
    count += 1


for idx, each in enumerate(mydata):
    if each % 2 == 0:
        continue
    else:
        mydata.pop(idx)

print("The resultant list is:")
print(mydata)

#End of the Program