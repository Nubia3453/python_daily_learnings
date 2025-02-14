# comparing data from files
import difflib
read1= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file1.txt','r')
read2= open(r'E:\Python_coding_stuff\101_python_practice\day_24\file2.txt','r')
para1=read1.readlines()
para2=read2.readlines()

print(para1)
print(para2)
print(difflib.SequenceMatcher(None,para1,para2).ratio())

# compare 
matches = difflib.SequenceMatcher( 
    None, para1, para2).get_matching_blocks() 
  
for ele in matches: 
    print(para2[ele.a:ele.a + ele.size])