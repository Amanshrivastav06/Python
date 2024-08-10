
from functools import reduce

# Map- Map applies a function to all the items in an input_list.
# MAP EXAMPLE -
l = [1,2,3,4,4]
square = lambda x : x*x
sqlist = map(square, l)
print(list(sqlist))

# FILTER - Filter creates a list of items for which the function returns true.
# FILTER EXAMPLE -

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#Reduce Filter - Reduce applies a rolling computation to sequential pair of elements.
def sum(a,b):
    return a + b

print(reduce(sum, l)) # ye reduce import kiya hai.