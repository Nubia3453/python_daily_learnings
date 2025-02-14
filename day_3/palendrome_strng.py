# *******************************************************************************
# Implement a program that checks if a given string is a palindrome
# *******************************************************************************
# A palindrome is a sequnce that reads the same forward and backward,
# it may be a word, phrase or a number. remeber only thing that metters here is sequence irrespective to
# case of letters.

word_list = ["apple", "madam", "cherry", "Date", "Atta", "figure", 
             "deified" , "12321", "rotator","birD riB","taco cat"]

import random
# normalizing the input string to strip off spaces and lowercase all letters
user_string=random.choice(word_list).lower().replace(' ','')
if user_string==user_string[::-1]:
    print('Given string {} is palendrome'.format(user_string))
else:
    print('Given string {} is not palendrom'.format(user_string))


