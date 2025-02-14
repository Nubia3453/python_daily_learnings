
# *************************************************************
# minutes to hours and minutes calculator
# *************************************************************
# we need one user input, the value is non zero postive number.
# function give two values hours value and minutes value.

import random

def time_calculator(user_min):
    hour=(user_min//60)
    min=(((user_min%60)*60)//59)
    return(hour,min)

#input:
user_min=random.randint(-500,500)

#input validation and calculations:
if user_min <= 0:
    message="Error while processing, minutes value {} should be nonzero positive number".format(user_min)
    hours=0
    minutes=0
else:
    #calculations:
    hours=time_calculator(user_min)[0]
    minutes=time_calculator(user_min)[1]
    message=''

#output:
print('*'*17,'Here is results','*'*17)
print('Given Minutes:', user_min)      # display list
print('Hours: ', hours)   # display sum 
print('Mins:', minutes)  #display avarage
print(message)
print('*'*51)
