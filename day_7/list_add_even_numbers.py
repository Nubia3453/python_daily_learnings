
# *****************************************************************
# Create a list and add, remove, and update elements.
# *****************************************************************

# create list: give items inside square brackets which considered as list.
words=['issue', 'believe', 'process', 'eight', 'artist', 'child']
empty_list=[]


# add items to it: append() and insert() method used to populate list. append will add item to it.
# insert() - adds item to specific index or location
# append() - adds items at end of existing list.

words.append('issue')
empty_list.append('new_item')
words.insert(3,'new_item')
print(words)


# remove specifc items: remove() and pop() these methods used to remove items from list
# remove() - here we spcify the item to remove.
# pop() - here we specify the index of item to remove.
words.remove('issue')
print(words)
words.pop(2)
print(words)

# update a specific items: this method uses index number and updating string/element.
another_list=['issue', 'believe', 'process', 'new_item', 'eight', 'artist', 'child', 'issue']
print(another_list)
another_list[2]='updated process'
print(another_list)


# this is another way to update and here we can specify what element to update accordingly all this happens.

index=words.index('process')

words.pop(words.index('process'))
words.insert(index,'updated')

print(words)






