# *******************************************************************************
# Create a function to reverse a given string
# *******************************************************************************
# her eis trick, till now i have been testing my code with manual input. 
# i am done with typing new sentence evrytime when i run code, so i decided to have some automation which will 
# generate sentence for me. the soultion is Faker. Faker is pakage generates strings.
# here faker is pakage and Faker is class.
from faker import Faker  

# so using this class we are creating an object called fake.
fake=Faker()
# here is main logic to reverse string
user_string=fake.sentence()
reversed_string=user_string[::-1]

print('*'*17,'Here is results','*'*17)
print('Given string: {}'.format(user_string)) 
print() 
print('Reversed string: {}'.format(reversed_string))   
print('*'*51)
