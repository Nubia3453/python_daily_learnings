from faker import Faker
fake=Faker()
senetnce= fake.sentence(10)
word=fake.word('noun')
list=[]
counter={}
for i in word:
    list.append(i)

list_2=[]


a=0
for i in list:
    a=list.count(i)
    if i not in list_2 and a > 1:
        list_2.append(i)
    counter[i]=a



print('*'*60)
print('Given word:', word)
print('Letters count in given word')
for key,value in counter.items():
    print(key,':',value)

print('repeated letter:',list_2)
print('*'*60)