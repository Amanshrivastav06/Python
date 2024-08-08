#6.Write a program to calculate the factorial of a given number using for loop.
# 5 = 5X4X3X2X1
# 4 = 4X3X2X1
n = int(input("enter the no :"))
product = 1
for i in range(1, n+1):
    product = product * i 

print(f"The factorial of {n} is {product}")