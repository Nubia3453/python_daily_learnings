# -----------------------------------------------------------------------------------------------
# Given a list of integers, find the sum of all positive numbers 
# -----------------------------------------------------------------------------------------------
# here the term positive integers are refered to the numbers that are greater than zero, and also not a zero.
# second thing, int menase we need to consider whole numbers only.

my_list=[37, -64, -52, 54, 70, 98, -21, -72, 94, 14]

print(sum(i for i in my_list if i > 0))