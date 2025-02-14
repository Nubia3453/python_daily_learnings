#----------------------------------------------------------------------------------
# Write a program to calculate simple interest.
#----------------------------------------------------------------------------------
#similer to compund intrest, just use formula and get answer.
# major inputs from user is pricipla amout, intrest rate, time.
# calculate intrest amunt = SI = p * (r/100) * t

priciple=3000 # principle amount
rate=5    #intrest rate per annum
time=10   #intreting yeras
simple_intrest= priciple * (rate/100) * time

print(simple_intrest)

print("*" * 11, "Simple intrest calculator", "*"*11)
print("Principle amount: ", priciple) 
print("Rate: ", rate ,"% per annum")     
print("Period: ", time, "Years")
print("*" * 50)
print("Caculculated Intrest Amount:", simple_intrest)
print("Final Amount after {} years:".format(time),(priciple+simple_intrest))
print("*" * 50)