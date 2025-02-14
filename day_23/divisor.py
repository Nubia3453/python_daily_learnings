# divisior is a number that divides another number without a remainder.
# Write a program that takes a number and prints all of its divisors.
import random
divisors = []
divisors_dict = {}
n=random.randint(-20,20)
if n > 0:
    for i in range(1,n+1): 
        if n%i == 0:
            divisors.append(i)
            divisors_dict[n]=divisors
    print(divisors_dict)
else:
    print(f'{n} Try non zero positive number')
