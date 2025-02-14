import random
number=random.randint(0,100)
flag=False
for i in range(2, number):
    if (number % i) == 0:
        flag = True # if factor is found, set flag to True
    # break out of loop
    break

if flag:
 print(f"{number}, is not a prime number")
else:
 print(f"{number}, is a prime number")

