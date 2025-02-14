from faker import Faker
import datetime

#define variables:
fake=Faker()
counter=0
details=[]
log_header='*'*50
log_trailer='*'*50

def open_csv_file():
    csv_file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\test_file.csv", 'w')
    return csv_file

def open_log_file():
    log_file=open(r"E:\Python_coding_stuff\101_python_practice\day_9\log.txt", 'w')
    return log_file

def file_open():
    open_csv_file()
    open_log_file()
    return 

outfile=open_csv_file()
outfile_logfile=open_log_file() 

def generate_and_write_data():
    global counter
    global details
    header='Name,Address,,City,State,Zipcode,Company,Job'
    outfile.write(header)
    for i in range(100):
        details.append(fake.name())
        details.append(fake.address())
        details.append(fake.city())
        details.append(fake.state())
        details.append(fake.zipcode())
        details.append(fake.company())
        details.append(fake.job())
        outfile.write('\n')
        # coverted list into string:
        details_string=str(details)

        # formatting detailsstring such as remove prefix and suffix braket, remove quote mark.
        details_string=details_string.removeprefix('[')
        details_string=details_string.removesuffix(']')
        details_string=details_string.replace("'","")

        #writting formatted string to output file:
        outfile.write(details_string)
        
        #writing logs to log file:
        outfile_logfile.write('\n')
        outfile_logfile.write(str('Now writing:' + str(details)))

        # counter to count no of lines written
        counter+=1

        #intialize list to append new data for next loop
        details=[]
    return 

def write_log_header():
    date=('Log date: {}'.format(datetime.datetime.now()))
    file_name=('Opening file: '+str(outfile.name))
    outfile_logfile.write('*'*100)
    outfile_logfile.write('\n')
    outfile_logfile.write(date)
    outfile_logfile.write('\n')
    outfile_logfile.write(file_name)
    outfile_logfile.write('\n')
    outfile_logfile.write('*'*100)
    return

def write_log_trailer():
    outfile_logfile.write('\n')
    outfile_logfile.write('*'*100)
    no_of_lines=('No of lines written: {}'.format(counter))
    outfile_logfile.write('\n')
    outfile_logfile.write(no_of_lines)
    outfile_logfile.write('\n')
    outfile_logfile.write('*'*100)

def close_file():
    outfile.close()
    outfile_logfile.close()
    return

def main_function():
    file_open()
    write_log_header()
    generate_and_write_data()
    write_log_trailer()
    return

main_function()