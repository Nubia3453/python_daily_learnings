# **********************************************************
# Replace all spaces in a string with underscores.
# **********************************************************
# Here the input is just simple string given by user, string operation replace() fucntion usedto 
# replace spaces with underscore.

from faker import Faker
fake=Faker()

user_string=fake.sentence()
def space_replace_(user_sentence):
    user_sentence=user_sentence.replace(' ','_')
    return user_sentence
user_string=fake.sentence()
print(space_replace_(user_string))