from faker import Faker
import datetime
file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\test_file.txt", 'w')

fake=Faker()

details=[]
# generate fake details:
for i in range(1):
    details.append(fake.name())
    details.append(fake.address())
    details.append(fake.city())
    details.append(fake.state())
    details.append(fake.zipcode())
    details.append(fake.company())
    details.append(fake.job())

details_tuple=tuple(details)


print(datetime.datetime.now())
print("*"*50)
print('Name: ',details_tuple[0])
print('Address: ',details_tuple[1])
print('City:',details_tuple[2])
print('State: ',details_tuple[3])
print('Zip code:',details_tuple[4])
print('Compnay: ',details_tuple[5])
print('Job: ',details_tuple[6])
print("*"*50)

file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\test_file.txt", 'w')
eval(file)
name='Name: ' + str(details_tuple[0])
log_date=str(datetime.datetime.now())
file.write(log_date)
file.write('\n')
file.write(name)
file.close()
