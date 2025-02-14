#*******************************************************************************
# Create a program that takes a temperature in Celsius and converts it to Kelvin
#*******************************************************************************

#this is simple formula based code, just use converion formula and you will get answer.

# formula = kel=cel+273.95
# instead of putting value manuly everytime, lets automate the testing part using automated generated numbers.
#for this i am using randomly generated numbers using random library.

#edge cases: the absolute zero temperature in kelvin is 0 which equals to -273.15 in cecius, so any value below 
# -273.15 can not be measured.

import random

user_input=random.randint(-1000,1000)

# take temperature in celcius:
temp_cel=float(user_input)

#convert to kelvin:
if not temp_cel <= -273.15:
    temp_kel=(round(temp_cel+273.15,2))
else:
    temp_kel='Error v- Temprature is below absolute zero value'

print('*'*17,'Here is results','*'*17)
print('Temperature: {} ℃'.format(temp_cel))   # display temp in celcius
print('Temperature: {} ºK'.format(temp_kel))   # display temp in kelvin
print('*'*51)