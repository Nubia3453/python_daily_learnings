# *****************************************************************
# Concatenate two lists into one.
# *****************************************************************
# combine two lists using extend() function.

# import requred libraries:
import random
list_1=[]
list_2=[]

# add items to list:
for i in range(6):
    list_1.append(random.randint(1,50))
    list_2.append(random.randint(50,100))

# prepare lists:
    # 1. take copy of original l ist before editing.
list_1_copy=list_1.copy()
    # 2. extend main list using another list:
list_1.extend(list_2)   

# diplay lists:

print('********************************************************************')
print("list 1:",list_1_copy)
print("list 2:",list_2)
print("combined lsit: ", list_1)
print('********************************************************************')



