# Sort a dictionary by keys and values.
my_dict={}

from faker import Faker
import random
fake=Faker()

for j in range(0,11):
    my_dict[random.randint(1,10)]=fake.name()
print(my_dict)

