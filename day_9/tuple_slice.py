# ***********************************************
# Slice a tuple and print the result.
# ***********************************************
# slicing refers to accessing a spcific lenth of tuple.

import random

# create a list:
my_list=[]
for i in range(12):
    my_list.append(random.randint(0,50))

# convert list to slice:
my_tuple=tuple(my_list)
a=random.randint(0,12)
b=random.randint(0,12)

print(my_list[a:b])