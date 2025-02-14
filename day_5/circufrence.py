# *******************************************************************
# Calculate the area and circumference of a circle given its radius
# *******************************************************************

# consider 2 formulas 
#     1. circumfrence = 2 x pi x r
#     2. area = pi x r^2

# we have input as radius, and valuse should be non zero positive numbers.
# so 2 checkpoints, 1 non zero, positive numbers.

# check user input, in return we will get either value or error message:
import math
import random

# defining constant valuse:
pi=math.pi
message=''
area=0
circumfrence=0
pi


def calculate_circumfrenec(radius):
    circumference=2*pi*radius
    return circumference

def calculate_area(radius):
    area=pi*(radius**2)
    return area

# main fuction to calculate area and circumfrence using radius:
def main_function(user_input):
    if user_input <= 0:
        area = 0
        circumfrence = 0
        message= 'Error, Please enter non zero positve radius value.'
    else:
        radius=user_input
        area=calculate_area(radius)
        circumfrence=calculate_circumfrenec(radius)
        message=''
    return user_input,area,circumfrence,message


# testing part
#generating radius values using random value generator.
user_input=random.randint(-99,99)

results=main_function(user_input)
radius=results[0]
area=results[1]
circumference=results[2]
message=results[3]

# displaying results
print('*'*17,'Here is results','*'*17)
print('Radius:', radius)      # display list
print('Area: ', round(area,2))   # display sum 
print('Circumfrence:', round(circumference,2))  #display avarage
print(message)
print('*'*51)








