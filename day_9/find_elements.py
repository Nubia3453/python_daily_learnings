# ***********************************************
# Write a program to merge two tuples.
# ***********************************************

# usualy we use in keyword to check element exist in given group.
# another method which is correct method, used specialy for tupples. is _contains_()
import random

# create a list:
my_list=[]
for i in range(12):
    my_list.append(random.randint(0,50))

# convert list to tuple:
my_tupple_1=tuple(my_list)
a=random.randint(0,50)
verify= my_tupple_1.__contains__(a)

if verify==True:
    possition=my_tupple_1.index(a)
    message=('value {} found in tupple at posstion {}'.format(a,possition))
else:
    message=('Error! given value {} not found in tupple'.format(a))
# display results
print('*'*50)
print('given tuple :',my_tupple_1)
print(message)
print('*'*50)