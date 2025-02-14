
# a string, has two smiler characters, identify it, and count the no of characters between them


str = 'identify'
list=[]
for i in str:
    list.append(i)

for j in range(1,len(list)):
    if list[0] == list[j]:
        print(list[0],list[j],j-1)






