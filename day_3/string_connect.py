# ********************************************************************************
# Given a list of names, concatenate them into a single string separated by spaces
# ********************************************************************************

# okay so this code is not that much complicated as it looks like,
# but here some extra steps added just to text the code, code takes input as a string,
# this is faker pakage, this will generate randomly generate words, and using for loop we are creating a list of given words.

import random
from faker import Faker

# this step is to generate number, that will define length of word list.
number=random.randint(2,10)

word=Faker()
# this step is to generate word list
word_list=[]
for i in range(number):
    word_list.append(word.word())

# this is actual code where we are joining words with spaces as delimiter.
word_string=' '.join(word_list)

print('*'*17,'Here is results','*'*17)
print('No of words generated: {}'.format(number) )
print('Given word list: {}'.format(word_list)) 
print('Genrated string: {}'.format(word_string))   
print('*'*51)


