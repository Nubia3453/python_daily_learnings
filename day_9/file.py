import datetime
file=open(r'E:\Python_coding_stuff\101_python_practice\day_10\test.txt', 'w')

def write_data():
    date=(datetime.datetime.now())
    file.write(str(date))
    file.write('\nhello world')
    file.close()
    return 


write_data()

    



