# -----------------------------------------------------------------------------------------------
# Implement a program that swaps the values of two variables
# -----------------------------------------------------------------------------------------------
# here we are reassigning values of variable to each others.
# this can achived by two methods.
# first is using temp variable, first assign second value to temp, now assign first value to second, so that it will be overwritten
# now assign temp value to first so first value is over written by this way we have values swapped.

variable_1 = 10
variable_2 = 20
print(variable_1,variable_2)

#swaping using third variable
temp_var = variable_2
variable_2 = variable_1
variable_1=temp_var
print(variable_1,variable_2)


#swaping using pythoin bukitin varibale declaration method.
variable_1 = 10
variable_2 = 20
variable_1,variable_2 = variable_2,variable_1
print(variable_1,variable_2)
