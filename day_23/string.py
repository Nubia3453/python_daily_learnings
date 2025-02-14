# consider this string 'elderberry'

# write a code that count no of letters lies in between two similler letters.
# for example in 'elderberry' there are 4 letters between 'e' and 'r' which are 'l','d','e','b'

# step 1: create a list of all the letters in the string
my_list=[i for i in 'elderberry']
print(my_list)
# step 2: find the index of the first letter
n=0
for i in my_list:
    print(i)
    for j in my_list[n:]:
        if i == j:
            print(j)
            exit
        n+=1
        exit
    exit


# step 3: find the index of the second letter
# step 4: print the letters between the two indexes
# step 5: print the count of the letters between the two indexes
