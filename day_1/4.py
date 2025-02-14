# -----------------------------------------------------------------------------------------------
# Create a program that takes a sentence as input and counts the number of words in it
# -----------------------------------------------------------------------------------------------
# so here i am accepting only one argument that is string.
# and core logic is to convert that string into a list by delimituing by space

# this is tricky part, any sentence will not have only space, it may also have comma, inverted comma, semi colon, colon, and other marks.
# those all need to be converted into single common delimiter that is space.

# and furthur after replacing all with space this string isplsitted and stored as a list.
# and length of this list will gives us word count.
import re
sentence = 'A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search.'

# counter=[]
# "," in sentence
# if True:
#     sentence=sentence.replace(",","")

# "!" in sentence
# if True:
#     sentence=sentence.replace("!","")

# ";" in sentence
# if True:
#     sentence=sentence.replace(",","")

# print(sentence)

# my_list=sentence.split(' ')
# print(len(my_list))

# above code was full of if staments, no with help of regiler expression
# we can replace mutiple characters with common delimiter within single line of code

sentence=re.sub('[,;:!?]','', sentence)
counter_list = sentence.split(' ')
print(("given sentnec has word count of {}".format(len(counter_list))))


