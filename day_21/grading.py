# Implement a simple grading system based on marks

# lets define marks range and grades
# 85-100 A
# 70-84 B
# 55-69 C
# 40-54 D
# 0-39 F
import random
marks=random.randint(0,100)
# create grading system:
if marks >= 85 and marks <= 100:
    grade="A"
elif marks >= 70 and marks <= 84:
    grade="B"
elif marks >= 55 and marks <= 69:
    grade="C"   
elif marks >= 40 and marks <= 54:
    grade="D"   
else:   
    grade="F"

# display results
print(f"marks: {marks} grade: {grade}")


