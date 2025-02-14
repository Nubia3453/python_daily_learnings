#----------------------------------------------------------------------------------
# Find the square root of a number.
#----------------------------------------------------------------------------------
# this one is easy, just have to find square root of number.
# now few conditions, number should be non zero and positive whole number.
# two ways we can achive this,
    # first is simple x^0.5 
    # second is using built in pakage and function
import math
num=float(input('Your number: '))
# this is advance method.
if num>0:
    print(round(math.sqrt(num),2))
else:
    print('Number should be non zero positive number')

# this is simple method.
print(round(num**0.5,2))
