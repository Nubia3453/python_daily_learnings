from faker import  Faker
fake=Faker()
para=fake.paragraph()

# create a output file

file=open(r"E:\Python_coding_stuff\101_python_practice\day_20\para.txt", "w") #open in write mode

# write para to file.

file.write(para)


