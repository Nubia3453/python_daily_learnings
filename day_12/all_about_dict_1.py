# dictonaries used to store data in form of key-value pair, key act as index or pointer for the perticuler value.
# any value can be easily accessed by its key.
# {} this is sign of dictonaries and dict() is function to create dictonaries.

my_dict=dict(name='Vinayak', place='Sangli', contact=1234667890)
# here name,place and contact are variables to store thier respective values.


# since dictonaries are mutable, that meance any point of time the contents can be aleterd and updated.
#suppose if any new filed to be added.

my_dict['email'] = 'testemail.gamil.com'
# also the job details need to add

my_dict['Occupation']='Private Job'

# now lets update few fileds. same way that the new data is added.
# lets update contact details.

my_dict['contact']= '2546543543'
#also
my_dict['email']='thisismyemail.com' 

print(my_dict)

# basic syntax my_dict['key']='value'
squares={}
for value in range(5):
     squares[value]= (value**2)
print(squares)

# since we have two dict, lrts try to delete one of them.
# this will delete just specified key and its corrosponding value
del squares[1]
print(squares)
# this will delete whole dictonary
del squares

print(my_dict)

# pop will return a value of a specified key that was deleted.
# for example key called name is deleted, then it will return the its respective value
what=my_dict.pop('name')
print(what)

# while popitem() will remove last added key-value pair

what=my_dict.popitem()
print(what)

# dict[key]=value
import random
from faker import Faker
fake=Faker()
random_numbers={}

deatil=['1','Victoria Ramos']

for value in range(5):
     name=fake.first_name()
     #value=random.randint(1,10)
     random_numbers[name]=deatil

contact={}
contact=random_numbers.copy()

for key,value in random_numbers.items():
    print([random_numbers.values()])



     
     