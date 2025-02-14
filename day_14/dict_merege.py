# Merge two dictionaries.
list=[]
my_dict={}
my_dict_2={}
import random

for i in range(1,10):
    list.append(random.randint(1,20))

for i in list:
    my_dict[i]=(i*2-i**2)


for i in range(1,10):
    list.append(random.randint(1,20))

for i in list:
    my_dict_2[i]=(i*2+i**2)

#using comprehension methid
extended = {**my_dict, **my_dict_2}
print(extended)

#using union method
print(my_dict | my_dict_2)