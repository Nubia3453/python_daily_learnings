# Remove duplicates from a list using a set.

# create list:
import random
my_list=[]
for i in range(10):
    my_list.append(random.randint(1,30))

print(my_list)

#remove duplicates by converting list to set:

my_set=set(my_list)

print(my_set)