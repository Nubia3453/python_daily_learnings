from faker import Faker
import random
fake=Faker()
student={}
result=[]
file=open(r'E:\Python_coding_stuff\101_python_practice\day_16\data\student.txt','w') 
for i in range(1,51):
    student[i]=fake.name()

std_cont=0
sum_mark1=0
sum_mark2=0
sum_mark3=0
header='''Roll No,Student Name,Language1,Language2,Language3,Total'''
file.write(header)
file.write('\n')
total=0
for key,value in student.items():
    std_cont=std_cont+1
    mark1=random.randint(50,99)
    sum_mark1=sum_mark1+mark1
    mark2=random.randint(50,99)
    sum_mark2=sum_mark2+mark2
    mark3=random.randint(50,99)
    sum_mark3=sum_mark3+mark3
    total=mark1+mark2+mark3
    marks=[(key),
           str(value),
           str(mark1),
           str(mark2),
           str(mark3),
           str(total)]
    line=str(marks)
    line=line.replace('[','')
    line=line.replace(']','')
    line=line.replace("'",'')
    file.write(line)
    file.write('\n')

#file.write(str(str(std_cont)+", ,"+str(sum_mark1)+','+str(sum_mark2)+','+str(sum_mark3)+','+str(total)))

file.close()

    

