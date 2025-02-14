# *****************************************************************
# find largest and smallest number in a given string
# *****************************************************************
# this time code is simplyfied using inbuilt functions max() and min()
import random

# create a list
my_numbers=[]

# add items
for i in range(6):
    my_numbers.append(random.randint(1,50))

# find smallest and largest number:
print('my list:', my_numbers)
print('smallest number:', min(my_numbers))
print('largest number:', max(my_numbers))


