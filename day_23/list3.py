# suppose we have a list of words, copy the words from the list to a new list in reverse order, 
# remebder the order of letters within should be reversed.


#import random   
list1 = ['apple','banana','cherry','date','elderberry','fig','grape','honeydew','kiwi','lemon']
list2 = []
for i in list1:
    list2.append(i[::-1])
list2=list2[::-1]
print(list2)


