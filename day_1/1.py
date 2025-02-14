#Example Questions:
#Q 1: Write a Python program to print "Hello, World!"
#directly display string using print function
print('hello world!')

#assign a string value to a variable and print that variable.
#what makes this diffrent, here we have fexlibatlity to chnage the string within variable
#itself, so it willbe printed any value which that variable hlds

my_string='Hello World'
print(my_string)

#ask the custom string from user and print it.
my_string=input("give you custome string here")
print(my_string)

#Q 2: Calculate the sum of two numbers entered by the user.
#sum=num1+sum2
num1=int(input("First number: "))
num2=int(input("Second number: "))
sum=num1+num2
print(" ", num1)
print("+", num2)
print("-" * (len(str(num1))) + ("-" *  3))
print(" ", sum)

#Q 3: Convert temperature from Celsius to Fahrenheit.
# basic formula is temp_Far=temp_cel * (9/5) + 32

temp_cel=float(input("Your temp here: "))
temp_Far=temp_cel * (9/5) + 32
print(round(temp_Far))


