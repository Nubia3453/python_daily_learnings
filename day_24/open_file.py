# write a code to open a text file and read the content of the file.
# create file
from faker import Faker

fake = Faker()

file1= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file1.txt','w')
file2= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file2.txt','w')

string1 = fake.sentence()
file1.write(string1)
string2 = fake.sentence()
file2.write(string2)

file1.close()
file2.close()
#step1: open the file

read1= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file1.txt','r')
read2= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file2.txt','r')

print(read1.readline())
print(read2.readline())
#step2: read the content of the file

#step3: print the content of the file

#step4: close the file