#.8 Write a python function to print multiplication table of a given number.

def multiplication(n):
    product = 1
    for i in range (1 , 11):
        print(F"{n} X {i} = {n*i}")
       
s= int(input("enter the number: "))
print(f"the table of: {s}")
multiplication(s)