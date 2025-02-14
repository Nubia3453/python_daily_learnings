# *****************************************************************
# find largest and smallest number in a given string
# *****************************************************************
import random

# create a list
my_numbers=[]

# add items
for i in range(6):
    my_numbers.append(random.randint(1,50))
index=len(my_numbers)
my_numbers.sort()
# find smallest number:
smallest_number=my_numbers[0]

# find largets number:
largest_number=my_numbers[(index-1)]

# display results
print('my list:', my_numbers)
print('smallest number:', smallest_number)
print('largest number:', largest_number)


