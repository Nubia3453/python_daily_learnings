# Print numbers from 1 to 10 using a loop.
file=open('output.txt',"w")
for number in range(1,11):
    print(number)
    file.write(str(number)+'\n')


