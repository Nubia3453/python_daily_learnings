import re

txt = "The rain in Spain"
x = re.findall("", txt)
print(x)


txt = "The rain in Spain"
formatted_txt=txt.lower().replace(' ','')
x = re.finditer(r"[a-z]", formatted_txt)
count=0
for i in x:
    print(i)
    count+=1

print(count)