#1. Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))
num4 = int(input("Enter the number4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"{num1}, is Greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"{num2}, is Greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"{num3}, is Greatest")
elif(num4>num1 and num4>num2 and num4>num3):
    print(f"{num4}, is Greatest")


