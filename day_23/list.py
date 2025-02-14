# can a list have multiple data types?
# Yes, a list can have multiple data types
choice = [1,3,5,2.3,5.6,'a','b','string','list',['list',1]]
my_list = []
import random
for i in choice:
    my_list.append(random.choice(choice))

print(my_list)

