# *****************************************************************************************
# Update a item from list with specific item.
# *****************************************************************************************

# create a list and display it to user.
my_list=['issue', 'believe', 'updated process', 'new_item', 'eight', 'artist', 'child']

old_list=my_list.copy()
# display intial messages and list to user.
print('*****************************************************************')
print('Hello!, here is list avaliable')
print(my_list)
print('*****************************************************************')


# user selection accepted here, the list item is accepted to be updated.
user_selection=input('item to remove: ')
index=my_list.index(user_selection)
my_list.pop(index)
# accept item to update with:
item_to_update=input('item to update with: ')

my_list.insert(index,item_to_update)
print('*****************************************************************')
print("Old list:",old_list)
print("Updated list:",my_list)
print('*****************************************************************')
