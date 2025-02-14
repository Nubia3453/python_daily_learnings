# largest number among given 3 numbers:
import random

a=random.randint(1,100)
b=random.randint(1,100)
c=random.randint(1,100)

def largest_number(a,b,c):
    if a==b or b==c or a==c:
        message="error while processing numbers"
    else:
        if a > b and a > c:
            message=f"{a} is largets"
        if b > c and b > a:
            message=f"{b} is largest"
        if c > a and c > b:
            message=f"{c} is largest"
    return message

print(a,b,c)
print(largest_number(a,b,c))