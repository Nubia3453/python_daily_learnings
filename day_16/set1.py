import random
set_1 = {2, 12, 4, 10, 3}
set_2 = {11, 15, 2, 9, 10}
set_3 = {2,5,10 }
print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
set_1.update(set_2)
print(set_1)
set_1.intersection_update(set_3)
print(set_1.symmetric_difference(set_2))

set_1.difference(set_3)

print(set_1)

print(set_1.issubset(set_3))