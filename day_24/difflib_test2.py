# comparing data from files
import difflib
read1= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file1.txt','r')
read2= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file2.txt','r')
para1=str(read1.readlines())
para2=str(read2.readlines())

# print(para1)
# print(para2)
# print(difflib.SequenceMatcher(None,para1,para2).ratio())

# compare 
differ = difflib.Differ()
diffrence = differ.compare(para2.splitlines(),para1.splitlines())
file = open(r"E:\Python_coding_stuff\101_python_practice\day_24\file.txt",'w')
for line in diffrence:
    file.write(str(line))
    print(line)
print(type(line))
line=line.replace('[','')
line=line.replace(']','')
print(line)