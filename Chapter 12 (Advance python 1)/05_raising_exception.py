# RAISING EXCEPTION - PROGRAM ke bich me ise use kar sakte hai 

a = int(input("enter a number: "))
b = int(input("enter a number: "))
if(b == 0):
    raise ZeroDivisionError("you enter zero which are not valid!! ")

else:
    print(f"the division a/b is {a/b}")

