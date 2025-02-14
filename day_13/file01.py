# Create a dictionary and perform basic operations (add, update, delete).
my_dict={}
from faker import Faker
import random
fake=Faker()
for j in range(1,10):
    my_dict[j]=fake.name()

print(my_dict)

my_dict[random.randint(1,10)]=fake.name()
print(my_dict)

new_dict=my_dict.copy()

my_dict.pop(random.randint(1,9))
print(my_dict)

new_dict.popitem()
print(new_dict)



