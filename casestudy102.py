'''
 Write a function to check if the year number is a leap year.
'''

#Beginning of the program:

x = input("Enter the year: ")
x = int(x)

if x % 100 == 0:
    if x % 400 == 0:
        print(x, " is a Leap Year!")
    else:
        print(x, " is not a Leap Year.")
else:
    if x % 4 == 0:
        print(x, " is a Leap Year!")
    else:
        print(x, " is not a Leap Year.")

#End of the Program.