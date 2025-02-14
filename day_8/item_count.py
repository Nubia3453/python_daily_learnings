# *****************************************************************
# Count the occurrences of a specific element in a list.
# *****************************************************************

# given list
items=[47, 12, 6, -5, -44, -44, 6, 12, 6, 42, 47, -44, -5, 5]

# display list and take input for speciifc item.
print('Here is list: ', items)
specific_item=int(input('Choose from list to count: '))

# check for reoccurense:
counter=0
for i in items:
    if i == specific_item:
        counter=counter+1

# display results:
print('*****************************************************************')
print("Selected item:", specific_item)
print("Occurence:", counter)
print('*****************************************************************')