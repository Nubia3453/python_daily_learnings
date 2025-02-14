# Sort a dictionary by keys and values.

my_dict ={}

for i in range(1,10):
    my_dict[i]=i**2

print(my_dict)

my_dict2={8: 648, 9: 18,3: 98, 4: 160,6: 36, 7: 491,1: 50}

print("Sorted by Key",sorted(my_dict2.items()))

print("sorted by Value",sorted(my_dict2.items(), key=lambda item:item[1]))

