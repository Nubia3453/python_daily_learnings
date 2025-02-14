# Sort a dictionary by keys and values.
list=[]
my_dict={}
import random

for i in range(1,10):
    list.append(random.randint(1,20))

for i in list:
    my_dict[i]=(i*2-i**2)

# print(my_dict)

# #sort by key

key_sort=sorted(my_dict.items())

# #sort by value

value_sort=sorted(my_dict.items(),key=lambda item:item[1])

# display results
print('*'*96)
print('mian dict:', my_dict)
print('sorted by key',key_sort)
print('sorted by value', value_sort)
print('*'*96)

