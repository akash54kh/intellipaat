'''
Create a list that has 10, 23, 4, 26, 4, 75, 24, 54 values and with the help
of while loop fetch the even numbers and print the numbers.
'''

#Start the program.

mylist = [10, 23, 4, 26, 4, 75, 24, 54]
counter = 0

while counter < len(mylist):
    if mylist[counter] % 2 == 0:
        print(mylist[counter])
    counter += 1

#End of program.