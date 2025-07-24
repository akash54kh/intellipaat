'''
1. Create 1st tuple with values-> (10, 20, 30), 2nd tuple with values-> (40, 50, 60):
 a. Concatenate the two tuples and store it in “t_combine”
 b. Repeat the elements of “t_combine” 3 times
 c. Access the 3rd element from “t_combine”
 d. Access the first three elements from “t_combine”
 e. Access the last three elements from “t_combine”

2. Create a list 'my_list' with these elements:
 a. First element is a tuple with values 1, 2, 3
 b. Second element is a tuple with values “a”, “b”, “c”
 c. Third element is a tuple with values True, False

3. Append a new tuple - (1, 'a', True) to 'my_list':
 a. Append a new list - *“sparta”, 123+ to my_list

4. Create a dictionary 'fruit' where:
 a. The first key is 'Fruit' and the values are (“Apple”, “Banana”, “Mango”, “Guava”)
 b. The second key is 'Cost' and the values are (85, 54, 120, 70)
 c. Extract all the keys from 'fruit'
 d. Extract all the values from 'fruit'

5. Create a set named 'my_set' with values (1, 1, “a”, “a”, True, True) andprint the result.
'''

#Start of Program 01:

t1 = 10, 20, 30
t2 = 40, 50, 60

combine = list()
print()

for each in t1:
    combine.append(each)

for each in t2:
    combine.append(each)

t_combine = tuple(combine)
print(t_combine)

combine *= 3
t_combine = tuple(combine)
print(combine)

print("The third element of t_combine is", combine[2])
print("The first three elements are", combine[:3])
print("The last three elements are", combine[-3:])

#Start of Program 02:

print()
my_list = [ (1, 2, 3), ('a','b','c'), (True, False)]
print(my_list)

#Start of Program 03:

print()
my_list.append((1, 'a', True))
my_list.append(['sparta', 123])
print(my_list)

#Start of Program 04: 

print()
my_dict = {'Fruit':['Apple', 'Banana', 'Mango', 'Guava'], 'Cost':[85, 54, 120, 70]}
for each in my_dict.values():
    print(each)

#Start of Program 05:

print()
my_set = {1, 1, 'a', "a", True, True}
print(my_set)

#END of the Programs.
