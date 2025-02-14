# The Fibonacci sequence begins with the following 14 integers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ... 
# Each number, starting with the third, adheres to the prescribed formula.
import random
sequence=[0,1,1]
prev_num1=1
prev_num2=1
next_num=0
n=random.randint(1,20)
for i in range(1,n-2):
    next_num=prev_num1+prev_num2 # calculate next number is sequence
    sequence.append(next_num)
    # exchanging the values of prevous 2 numbers to calculate next number
    prev_num2=prev_num1
    prev_num1=next_num

message_string=str(sequence)
message_string=message_string.replace("[","")
message_string=message_string.replace("]","")
message=f"fisrt {len(sequence)} numbers is sequence are {message_string}"

print(message)