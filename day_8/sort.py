import random
my_list=[]
for i in range(6):
    my_list.append(random.randint(1,50))

asc=my_list.copy()
desc=my_list.copy()

asc.sort()
desc.sort(reverse=True)
print(asc)
print(desc)