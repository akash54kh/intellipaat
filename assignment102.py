'''
Take three user inputs and print the greatest number from those inputs
using if-else condition. Edge cases, if any, should also be handled.
'''

#Start of the program.

print("Enter any three numbers: ")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

mydata = [a, b, c]
g = max(mydata)

print("The greater of three is", g)

#End of program.