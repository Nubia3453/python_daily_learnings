import random
from faker import Faker
fake=Faker()
random_numbers={}

deatil=['1','Victoria Ramos']

for value in range(1):
     name=fake.first_name()
     #value=random.randint(1,10)
     random_numbers[name]=deatil

print(random_numbers)