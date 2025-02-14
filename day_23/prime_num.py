# prime number is a number that is greater than 1 and divided by 1 or itself only.

import random
c=0
n=random.randint(1,50)
if n > 1:
    for i in range (1,n+1):
        if n%i == 0:
            c+=1


if c <= 2:
    print(f'{n} is prime number')   
else:
    print(f'{n} is not a prime number')