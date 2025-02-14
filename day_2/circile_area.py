#----------------------------------------------------------------------------------
# Calculate the area of a circle given its radius.
#----------------------------------------------------------------------------------

# ask is simple, area of circle can be calculated by simple math formula
        # area = pie * d
        # or area = pie * r^2

# most common issue is definig exact value of pi, so its better to not to hard code but take advantage of 
# python librarires, from math library i have taken pi value.
import math
pi = math.pi

# accept radius from user and calculate area
rad=float(input('Radius = '))
area=pi * (rad**2)

# just formatting and display stuff.
print('*'*50)
print('radius = {} units'.format(rad))
print('*'*50)
print('area = {} sq units.'.format(round(area,2)))
print('*'*50)
