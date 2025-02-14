#----------------------------------------------------------------------------------
# Perform addition, subtraction, multiplication, and division of two numbers.
#----------------------------------------------------------------------------------

# here ask is simple, 4 algebric operations that means 4 outputs and 2 inputs.
# input can be float, integers and whole numbers only.

num1=float(input('enter first number: '))
num2=float(input('enter second number: '))
#addition
sum=num1+num2

#subtract
sub=num1-num2

#multiply:
multply=num1*num2

#division
# div=num1/num2
# now here is trick, we can not divide any number by zero so, we need to make sure that
# num2 is not zero.

if not num2 == 0:
    div=num1/num2

else:
    div='second number should be non zero value.'
print('*'*50)
print('first number: {}          second number: {}'.format(num1,num2))
print('*'*50)
print('addition: ', sum)
print('subtraction: ',sub)
print('multiplecation: ',multply)
print('division: ',div)
print('*'*50)