import random
import numpy as np
import pandas as pd
x=[]
user_number=random.randint(1,30)
for multipler in range(1,11):
    product=user_number*multipler
    x.append('{} x {} = {}'.format(user_number,multipler,product))
arrey=np.array(x)
dataset=pd.DataFrame(arrey)

print('Table is created, as below: ')


print('Want to export to CSV (y/n):' )
option = input("enter option: ")
if option=='y':
    dataset.to_csv(r"E:\Python_coding_stuff\101_python_practice\day_7\table.csv",index=False,header=None)
    print("Dataset exported successfulyy!")
else:
    pass
