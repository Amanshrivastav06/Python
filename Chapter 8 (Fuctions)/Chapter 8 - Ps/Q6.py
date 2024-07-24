#6. Write a python function which converts inches to cms.
# cm = inches * 2.54

def inches_to_cm(inches):
    return inches*2.54
n = float(input("Enter value in inches: "))
print(f"The correspondig value in cms is {inches_to_cm(n)}")