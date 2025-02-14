# there is a list of integers, copy the list to a new list in reverse order

# step 1: create a list of integers
import random

list1 = [random.randint(1, 100) for i in range(10)]
print(list1)
# step 2: copy the list to a new list in reverse order
# step 2.1: create a new list
list2 = []

#step 2.2: copy the list to a new list in reverse order
list2=list1[::-1].copy()

#step 2.3: print the new list
print(list2)

