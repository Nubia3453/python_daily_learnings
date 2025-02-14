# ***********************************************
# Convert a list into a tuple.
# Find the length of a tuple.
# ***********************************************

import random

# create a list:
my_list=[]
for i in range(6):
    my_list.append(random.randint(0,50))

# convert list to tuple:
my_tupple=tuple(my_list)

# display results:
print('*'*50)
print('Created list :', my_list)
print('Created tupple: ',my_tupple)
print('Class verification: ',type(my_tupple))

# display length of tupple:
print('Length: ',len(my_tupple))
print('*'*50)
