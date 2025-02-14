# *****************************************************************
# Write a program to find the sum and average of numbers in a list.
# *****************************************************************
# this is simple program soulution is just two formula away.
# import libraries if requred.
import random
# create a list:
my_list=[]     #initialize list

# add items to list:
for i in range(6):
    my_list.append(random.randint(-50,50))

# calculate sum:
sum=sum(my_list)

# calculate average:
average=round((sum/len(my_list)),2)


#display results:

print('***************************** Results ***************************')
print('List: ', my_list)
print('Sum of elements:' , sum)
print('Avaerage of elements:', average)
print('*****************************************************************')