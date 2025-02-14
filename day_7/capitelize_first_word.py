
# section: libraries **************************************
from faker import Faker
fake=Faker()

# section: variables **************************************
upper=[]
sentence=fake.sentence()

# section: core logic **************************************
splitted=sentence.split(' ')
for i in splitted:
    upper.append(i[0].upper()+i[1:])
joined=' '.join(upper)


# section: results **************************************
print('************************************************************************************')
print('This program return a string such that first letter of every word is capitelized.')
print('************************************************************************************')
print('Test input: ',sentence)
print('Result: ',joined)
print('************************************************************************************')