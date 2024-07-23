#6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
g = int(input("Enter the no: "))
if(g<=100 and g<=90):
    grade = "Ex"
elif(g<=90 and g<=80):
    grade = "A"
elif(g<=80 and g<=70):
    grade = "B"
elif(g<=70 and g<=60):
    grade = "C"
elif(g<=60 and g<=50):
    grade = "D"
elif(g<=50):
    grade = "F"
print(f"your grade is:{grade}")
