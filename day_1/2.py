#practice questions
# -----------------------------------------------------------------------------------------------
#Write a Python program to calculate the area of a rectangle given its length and width 
# -----------------------------------------------------------------------------------------------
#as we hve variable names avaliable to use, ltes use them as it is.
#first we will write basic program then we will expnad it to more advanced step
#basic program
#length: accpet lenghth from user
length=input("Enter length: ")
#width:accpet width from user
width=input("Enter width: ")
#calcilate area:
area_rect=length * width
print(area_rect)

#now this is basic program, but lets step back and make this program more efficent, and reliable.
# 1. User input needs to be float value.
length=float(input("Enter length: "))
width=float(input("Enter width: "))
area_rect=length * width
print("Area of given Rect  is: ", area_rect)

# 2. values have no unit specified, so spcify a generic unit as sq. unit 
length=float(input("Enter length: "))
width=float(input("Enter width: "))
area_rect=length * width
print("Area of given Rect : ", area_rect, "SQ Unit")

# -----------------------------------------------------------------------------------------------
# Create a program that takes a user's name and age as input and prints a greeting message 
# -----------------------------------------------------------------------------------------------

#so here we have 2 inputs to have from user, name and age. so lets assign same names to variables.
# now greeting meesage should contain our both variables as part of string. so we will have to integrate it.

name=input("Your name please: ")
age=input("your age please: ")
greetings="hello {} yo old {} fuck you".format(age,name)
print(greetings)

# -----------------------------------------------------------------------------------------------
# Write a program to check if a number is even or odd 
# -----------------------------------------------------------------------------------------------
# so basic logic is if given number is compltely devisibale by 2 and reminder is zero.
number=45
if number % 2 == 0:
    result="even"
else:
    result="odd"
print("Given number {} is {} number.".format(number,result))

# -----------------------------------------------------------------------------------------------
#Given a list of numbers, find the maximum and minimum values 
# -----------------------------------------------------------------------------------------------
# here we have one input and two output, input is list of numbers.

numbers=[37, -64, -52, 54, 70, 98, -21, -72, 94, 14]
print("--------------------------------------------------------------")
print("Given numbers are ", numbers)
print("--------------------------------------------------------------")
print("biggest number is ", max(numbers))
print("--------------------------------------------------------------")
print("smallest number is ", min(numbers))
print("--------------------------------------------------------------")

# -----------------------------------------------------------------------------------------------
#Create a Python function to check if a given string is a palindrome 
# -----------------------------------------------------------------------------------------------

#A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
# for example “civic” or “2002.”

# basic logic we apply here is to compare two strings one is original string and one is revered string.

str=input("Your text here: ")
if str == str[::-1]:
    msg="Given string '{}' is palindrome".format(str)
else:
    msg="Given string '{}' is not palindrome".format(str)    
print(msg)


# -----------------------------------------------------------------------------------------------
#Calculate the compound interest for a given principal amount, interest rate, and time period 
# -----------------------------------------------------------------------------------------------

# here problem statement is preety easy, two things need to consider, inputs and formula for compund intrest.

# looking at inputs:
# principal amount - this is initail ampount invested by investor, this could be any non zero value, mostly integers. 
# interest rate - intrest rate given on invested principal amount. this is fraction float non zero value mostly a percentage value such as 2% or 3.2 %.
# so this need to taken as if rate is 4.56% then rate = 4.56
# time period - 
# no of years - 

# compund intrest is calcu;lated either annualy, quarterly or semi annualy.
# x*n 
# here x is time period:
#     for annual x is 1
#     for semi anual x is 2
#     for quaterly x is 4
#     for monthly x is 12
# p = 8000
# r = 10
# x = 12 # this value is specified based on calculation method 
# n = 1

p=int(input("Principal amount: "))
r=float(input("Intrest rate per annum: "))
x=int(input("Rate calculation method: annual = 1, semi = 2, quarterly = 4, monthly = 12: "))
n=int(input("period for deposite, no of years: " ))
a = p * ((1 + (r/(x*100)))**(x*n))
c = a - p

print("*" * 80)
print("Principle amount: ", p) 
print("rate: ", r ,"per annum")     
print("Period: ", n, "Years")
print("*" * 80)
print("Caculculated amount: ", a)
print("Compund intrest :", c)


# -----------------------------------------------------------------------------------------------
# Write a program that converts a given number of days into years, weeks, and days
# -----------------------------------------------------------------------------------------------
# here we are using single input is no of days.
# for example 45 days.
# 1 week has 7 days so no of week is calculated by dividing days by 7
# no_of_weeks = days / 7
# same way 1 year has 365 days, so no years is calculated by dividing 365

day = int(input("Enter Days: "))
years=day//366
months=((day % 366)//30)
weeks=((day % 366)//7)
days=(day%366%30)
print("{} equals to {} years {} months {} weeks {} days".format(day,years,months,weeks,days)) 











