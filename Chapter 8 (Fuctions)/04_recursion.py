# Recursion = is a function which call itself.
'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
.
.
.
factorial(n) = n X n-1 X.....3X2X1

factorial(n) = n * factorial(n-1)

'''


def fact(n):
    if(n==1 & n==0):
        return 1
    return n*fact(n-1) 

# print("the fact is :", fact(1)) # without user defined

n = int(input("Enter the number: "))
print(f"The fact of this number is: {fact(n)}" )


 
