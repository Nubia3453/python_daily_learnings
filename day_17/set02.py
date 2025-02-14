# Write a program to find common elements between two sets.

import random

# create list and covert to set:

list1=[]
list2=[]

for i in range(6):
    list1.append(random.randint(1,50))
    list2.append(random.randint(1,50))

set1=set(list1)
set2=set(list2)

#findout common element:
common_elements=set1.intersection(set2)
# print(common_elements)

if common_elements.__len__() > 0:
    for i in common_elements:
        print(i)
else:
    print('no common elements found')

