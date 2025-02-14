# Create a set and perform union, intersection, and difference operations.

# create a set: create a set from a list
import random
my_list=[] 
my_list_2=[]
for i in range(10):
    my_list.append(random.randint(1,50))
my_Set_1=set(my_list)

for i in range(10):
    my_list_2.append(random.randint(1,50))
my_Set_2=set(my_list_2)

# convert set to list and list to set
# convert set to list
print('given set:',my_Set_1)
set_to_list=list(my_Set_1)
print('converted list:',my_Set_1)
print('my_Set_1:',type(my_Set_1),'set_to_list:',type(set_to_list))

# conert list to set:
my_set=set(my_list)
print('given list:',my_list)
print('coverted set:',my_set)
print('my set:',type(my_set),'my list:',type(my_list))

# perform union, intersection, and difference operations.

my_list_a=[]
my_list_b=[]  
# perfom union
for i in range(10):
    my_list_a.append(random.randint(1,50))
my_Set_1=set(my_list_a)

for i in range(10):
    my_list_b.append(random.randint(1,50))
my_Set_2=set(my_list_b)
print(my_Set_1)
print(my_Set_2)
print('union:',my_Set_1.union(my_Set_2))

#perform intersection
print('intersection:',my_Set_1.intersection(my_Set_2))

#perform diffrence
print('diffrence:',my_Set_1.difference(my_Set_2))

# check symetric diffrenec:

print('symetric diffrenec:', my_Set_1.symmetric_difference(my_Set_2))