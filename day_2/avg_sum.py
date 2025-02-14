#----------------------------------------------------------------------------------
# Given a list of numbers, find the sum and average.
#----------------------------------------------------------------------------------
# we could have hardcode the list, but as a python devloper,
# its better to take advantage of python libraries, hence here is simple loop 
# to create list of random numbers. here we have used random library.

# step 1: Create list of random numbers:
import random
random_numbers=[]
for i in range(10):
     random_numbers.append(random.randint(1,50))

# step 2: Claculate and display results


