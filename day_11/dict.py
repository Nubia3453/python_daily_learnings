
#Create a dictionary and perform basic operations (add, update, delete).

# create dictonaru using dict() function. it takes argument in form of pair. one value is key and other is valur, both paired with = sign.
# key is variable name which stores value, so variable or key needs to be given wothout quotes and valueneed to be given within quote
import random
from faker import Faker
fake=Faker()
my_dict={}


def add_items():
    for _ in range(10):
        contact=[]
        name=fake.name()
        mobile=fake.phone_number()
        email=fake.email()
        contact.append(mobile)
        contact.append(email)
        my_dict[name]=contact
        contact=[]

def copy_dict():
    copy=my_dict.copy()
    return copy
#add_items()

def add_new_item():
        contact=[]
        name=input('Name:')
        mobile=input('Mobile:')
        email=fake.email()
        contact.append(mobile)
        contact.append(email)
        my_dict[name]=contact
        print('added successfuly')

add_new_item()
for key,values in my_dict.items():
    print(f'{key}:{values}')


