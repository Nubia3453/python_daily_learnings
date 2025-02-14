# ***********************************************
# Write a program to merge two tuples.
# ***********************************************
import random

# create a list:
my_list=[]
for i in range(12):
    my_list.append(random.randint(0,50))

# convert list to tuple:
my_tupple_1=tuple(my_list[0:7])
my_tupple_2=tuple(my_list[7:12])

# combine tupple:
combined_tuple=my_tupple_1.__add__(my_tupple_2)

# display results:
print('*'*50)
print('tupple 1 :',my_tupple_1)
print('tupple 2: ',my_tupple_2)
print('combined tupple: ',combined_tuple)
print('*'*50)


