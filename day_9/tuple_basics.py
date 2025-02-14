# ***********************************************
# Create a tuple and access its elements.
# ***********************************************

# tupple is inmutable collection of elements. once we create a tupple can not be modified.
# one tupple can be concatinated with another, but a single element can not be added to tupple.

# create atuuple:
my_tupple=(12,546,98769,6584,654)
my_anothet_tupple=(4654,6546,56463,5163)
combined_tupple=my_anothet_tupple.__add__(my_tupple)

# access elements:
import random
a=random.randint(0,4)
b=random.randint(0,3)
c=random.randint(0,8)
print('{} th element: '.format(a),my_tupple[a])
print('{} th element: '.format(b),my_anothet_tupple[b])
print('{} th element: '.format(c),combined_tupple[c])