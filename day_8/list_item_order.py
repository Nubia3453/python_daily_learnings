# *****************************************************************
# Write a program to find the sum and average of numbers in a list.
# *****************************************************************
# this is simple program soulution is just two formula away.
# import requred libraries:
import random
#create list
my_list=[]

# add elements:
for i in range(6):
    my_list.append(random.randint(-50,50))

random_numbers=my_list.copy()
#order items:
# here is trick we need two saperate lists to store assending and reverse ordered items.
assending_order=my_list.copy()
descending_order=my_list.copy()
assending_order.sort()
descending_order.sort(reverse=True)
# display results:

print('***************************** Results ***************************')
print('List: ', random_numbers)
print('Acesnding order:' ,assending_order)
print('Descending order: ', descending_order)
print('*****************************************************************')
