# *****************************************************************
# Create a function to count the number of vowels in a given string
# *****************************************************************

# import all requred libraries.
import re
from faker import Faker
fake=Faker()
# *****************************************************************
# create a sample input string using faker.sentnce() pakage

# sample_string=fake.sentence()

# *****************************************************************
#  this will create a list of all the vovels found in sample string, main list contains 5 sublists 
# each sublist assigned to each vovel.

pattern=['a','e','i','o','u']
result=[]
def vowel_extractor(test_input):
    c=0
    for i in pattern:
        result.append(re.findall('{}'.format(i),test_input))
    return result

# ***************************************************************** 
# for loop to count each vovels in given list:
# here is trick, the main list is consist of sub list in it, for all5 vovels.
# i needed to index the gien list propelry to find out matche value.
# for example i need to find vovel 'e' in given main list so i needed to index main list to index=1 as e is second vovel.
# variable 'c' is used for indexing purpose.
# and 'i' is used for iterate vovel through pattren list.
# for each iteration c will point rsepective index list and i will point to corrosponding vovle from pattern.
# *****************************************************************

# here is code to display results:
# total=0
# for i in pattern:
#     counter=result[c].count(i)
#     c+=1
#     total=total+counter

# print('Total Vovels=', total)
# *****************************************************************

def vowel_counter(result):
    total=0
    for i in pattern:
        counter=result[c].count(i)
        c+=1
        total=total+counter
    return total

test_input=fake.sentence()

output=vowel_counter(test_input)
print('Test case:',test_input)
print('Result:',output)