from faker import Faker
import datetime

# file open/close operations:
log_file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\log.txt", 'w')
csv_file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\test_file.csv", 'w')

#define variables:
fake=Faker()
counter=0
details=[]
log_header='*'*50
log_trailer='*'*50
file_name='File Name: '+ str(csv_file.name)

# writing header to csv file:
header='Name,Address,,City,State,Zipcode,Company,Job'
csv_file.write(header)

# writing details to log file:
log_file.write(log_header)
log_file.write('\n')
log_file.write(file_name)
log_file.write('\n')
log_file.write(log_header)


for i in range(100):
    details.append(fake.name())
    details.append(fake.address())
    details.append(fake.city())
    details.append(fake.state())
    details.append(fake.zipcode())
    details.append(fake.company())
    details.append(fake.job())
    csv_file.write('\n')
    # coverted list into string:
    details_string=str(details)

    # formatting detailsstring such as remove prefix and suffix braket, remove quote mark.
    details_string=details_string.removeprefix('[')
    details_string=details_string.removesuffix(']')
    details_string=details_string.replace("'","")

    #writting formatted string to output file:
    csv_file.write(details_string)
    
    #writing logs to log file:
    log_file.write('\n')
    log_file.write(str('Now writing:' + str(details)))

    # counter to count no of lines written
    counter+=1

    #intialize list to append new data for next loop
    details=[]


log_file.write('\n')
line_written='No of lines written: '+str(counter)

# writing other log details:
log_file.write('\n')
log_file.write(log_header)
log_file.write('\n')

# writing count of total lines written to log file.
log_file.write(line_written)
log_file.write('\n')
log_file.write(log_trailer)

# close files after writing data:
csv_file.close()
log_file.close()
