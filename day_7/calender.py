import calendar
import numpy as np
import pandas as pd
cal=[]
year=2024
month=0
for i in range(12):
    month+=1
    cal.append(calendar.month(year,month))


arrey=np.array(calendar.month(year,month))

dataframe= pd.DataFrame(cal)


print(dataframe)

dataframe.to_csv(r"E:\Python_coding_stuff\101_python_practice\day_7\calender.csv")





