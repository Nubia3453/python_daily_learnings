# factorial is a function that takes an integer, n, as a parameter and returns the factorial of n.
# factorials of numbers are the product of all positive integers less than or equal to n.

# factorial of 5 is 5*4*3*2*1 = 120

# Write a function that calculates the factorial of a number using a loop and writes the result to a file called factorial.txt.
# 
import random
factorials=[]
n=random.randint(0,10)
fact=1
result={}
if n == 0:
    result[n]=1
else:
    for i in range(1,n+1):
        fact=fact*i
        factorials.append(fact)
    result[n]=factorials
    
print(result)
