# Print a multiplication table for a given number.
import csv
file=open('table.csv',"w")
n=2
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    file.write(f"{n} x {i} = {n*i}" + "\n")