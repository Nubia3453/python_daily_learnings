# Check if a given year is a leap year.

# leap year is a year that is divisible by 4, but not by 100, unless it is divisible by 400.

# create list of years:
def year_list():
    list_years=[]
    for i in range(1900,2025):
        list_years.append(i)
    return list_years

# check year is leap year:
def check_leap_year():
    list_years=year_list()
    list_leap_years=[]
    leap_years={}
    for year in list_years:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            list_leap_years.append(year)
    leap_years["leap_years"]=list_leap_years
    return leap_years


# call mian function:
result=check_leap_year()

# display results
for key,value in result.items():
    print(key,value)