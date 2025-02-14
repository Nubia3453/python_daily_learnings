# check if givrn number is positive or negative or zero:
import random
num=random.randint(-100,100)
# check number:

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
