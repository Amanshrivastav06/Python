#5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [1,5,6,7,8,9,6]

def max(a,b):
    if(a>b):
        return a 
    return b

print(reduce(max, l))