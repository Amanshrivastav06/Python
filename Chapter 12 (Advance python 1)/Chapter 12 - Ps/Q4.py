#4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
if(b == 0):
    raise ZeroDivisionError("you enter zero which are not valid!! ")

else:
    print(f"the division a/b is {a/b}")


try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")

