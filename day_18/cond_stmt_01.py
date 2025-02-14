# Write a program to check if a number is even or odd
# even number is completley divisible by 2, meaning the remainder is 0
#fyi
# % is used to get the remainder of a division
# // is used to get the quotient of a division
import random
# accept a number from the user

num = random.randint(1, 100)
# check if the number is even or odd
if num % 2 == 0:
    message = f"{num} is even number\n"
else:
    message = f"{num} is odd number\n"


# write logs to a file
file=open ("logs.txt", "a")
file.write("\n")
file.write(message)
file.write("\n")
file.write(str(num//2))






