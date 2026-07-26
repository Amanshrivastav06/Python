# 1. Write a code to accept a string as input and output the same.#

A = input("Enter the string:  ")
print( A)


# 2.
# 
#  note - sometimes we have to accept multiples inputs in a single line.
# The way to accept multiple integers in a single line is to use the " SPLIT & MAP " FUNCTION.

# Split function  - breaks the input based on the separator -by default , it splits inputs
# separated by spaces in a single line into different inputs which you can assign to 
# differents variables.
# 
# Map function - converts each input into the defined datatype.
#  
# SYNTAX - a , b , c =  map(int , input().split())  # assigns integer input values to variables a,b,c .

'''2. Accept 3 space separated integers given in a line into 3 variables - A , b , c . 
print them out to a single line on the console

''' 
#sol .
  
A , B , C = map(int, input().split())
print(A, B, C)

