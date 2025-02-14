# read input file at from locatoion
import datetime
file_name=datetime.datetime.now().strftime("\%Y-%m-%d-%H-%M-%S"+".txt")
log_file=datetime.datetime.now().strftime("\log-%Y-%m-%d-%H-%M-%S"+".txt")
path = 'E:\\Python_coding_stuff\\101_python_practice\\day_20\\archive'
log_path = 'E:\\Python_coding_stuff\\101_python_practice\\day_20\\logs'
final= str(path+file_name)
log_final= str(log_path+log_file)

log=open(log_final,"x")

log.write(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

file=open(r"E:\Python_coding_stuff\101_python_practice\day_20\from\file.txt","r")
log.write("\n")
log.write("input file opened successfully")
file2=open(r"E:\Python_coding_stuff\101_python_practice\day_20\to\file.txt","w")
log.write("\n")
log.write("output file opened successfully")
archive=open(final,"x")
log.write("\n")
log.write("archive file opened successfully")
#copy to to folder
for lines in file:
    file2.writelines(file.readlines())
log.write("\n")
log.write("input file copied to output file successfully")
file.close()
log.write("\n")
log.write("input file closed successfully")
file2.close()
log.write("\n")
log.write("output file closed successfully")

file=open(r"E:\Python_coding_stuff\101_python_practice\day_20\from\file.txt","r")
# copy to archive folder
for lines in file:
    archive.writelines(file.readlines())  
log.write("\n")
log.write("input file copied to archived successfully")
file.close()
log.write("\n")
log.write("input file closed successfully")