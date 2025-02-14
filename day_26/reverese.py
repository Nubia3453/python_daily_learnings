# Write a function to reverse a string.

from faker import Faker
fake=Faker()

def revers(string):
    print(string[::-1])


# test input
string = fake.sentence()

# result
revers(string)