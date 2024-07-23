#Q1- write a program to store 5 fruits in a list entered by the user
fruits=[]
f1=input("Enter the fruit name: ")
fruits.append(f1)
f2= input("Enter the fruit name: ")
fruits.append(f2)
f3= input("Enter the fruit name: ")
fruits.append(f3)
f4= input("Enter the fruit name: ")
fruits.append(f4)
f5= input("Enter the fruit name: ")
fruits.append(f5)
fruits.sort()
print(fruits)

# USING FOR LOOP :
# print("Enter seven fruits: ")
# for i in range(7):
#     fruit=input(f"fruit{i+1}: ")
#     fruits.append(fruit)
# print("list of fruits enterd by user: ",fruits)

# USING WHILE LOOP:
# print("Enter seven fruits: ")
# i=0
# while (i<7):
#     fruit=input(f"fruit{i+1}: ")
#     fruits.append(fruit)
#     i+=1
#     # fruits.sort() - ye sort karne ke kaam aayega bs int value ke liye
# print("list of fruits enterd by user: ",fruits)
