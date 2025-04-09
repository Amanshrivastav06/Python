# 1.Write a Python program to sum all the items in a list.

n = [1,2,3,4,5]
print(sum(n))


# by function
def sum_list(list):
    sum = 0
    for i in list:
        sum =sum+i
    return sum

print(sum_list([1,2,3]))



# 2.Get Largest Number in List
 
def largest_num(list):
    largest = list[0]
    for i in list:
        if(i>largest):
            largest = i
    return largest
print(largest_num([1,2,4]))


# 3.Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_fun(list):
    count = 0
    for i in list:
        if isinstance(i, str):  # -- isinstance(i, str) checks whether the item is of type str.
            if len(i)>= 2 and i[0] == i[-1] :
            
                count +=1
    return count
            
print(count_fun(['abc', 'xyz', 'aba', '1221']))            


# 2 sra tarika ---

def c_string(string):
    count = 0
    for i in string:
         if len(i)>= 2 and i[0] == i[-1] :            
            count +=1
    return count

Sample_List =['abc', 'xyz', 'aba', '1221', 'ememe']
print(c_string(Sample_List))


#-- fun ke and fun ko call krna 

# def fun1():
#     return fun2()

# def fun2():
#     a = 1
#     b = 2
#     c = a+b
#     return a, b ,c
# a,b,c = fun1()
# print(f"the sum of A and B is = {c}" )



# calling func2 in func1
# def fun2(a, b):
#     c = a + b
#     return c

# def fun1():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
    
#     # Call fun2 to perform the addition
#     result = fun2(a, b)
    
#     return result

# # Call fun1
# result = fun1()

# # Output the result
# print(f"Result of addition: {result}")



# 2nd way--


def fun2():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    return a, b, c

def fun1():
    a, b, c = fun2()  # calling fun2 from fun1
    print(f"{a} + {b} = {c}")

# Call fun1 to start the process
fun1()

