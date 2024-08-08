#2- Write a program to accept marks of 6 students and display then in a stored manner
marks =[]
M1=int(input("Enter the marks: "))
marks.append(M1)
M2=int(input("Enter the marks: "))
marks.append(M2)
M3=int(input("Enter the marks: "))
marks.append(M3)
M4=int(input("Enter the marks: "))
marks.append(M4)
M5=int(input("Enter the marks: "))
marks.append(M5)
M6=int(input("Enter the marks: "))
marks.append(M6)
marks.sort()
print(marks)

# print("Enter 6 marks of student: ")
# i=0
# while (i<6):
#     M=int(input(f"M{i+1}: "))
#     marks.append(M)
#     i+=1
#     marks.sort()
# print("list of fruits enterd by user: ",marks)
