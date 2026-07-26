#5. Write a python function to print first n lines of the following pattern:
'''

***
** - for n = 3
* 

'''
# def star(n):
#     for i in range(0 , n+1):
#         print("*"*(n-i),end="")
#         print(" ")

# n = int(input("enter the number: "))
# print(f" n lines are: {star(n)}" )

def star(n):
    if(n==0):
        return
    print("*"*n)
    star(n-1)

n = int(input("Enter the number: "))
print(f"{n} lines are:")
star(n)







# using LOOP 
# n = int(input("enter the number: "))
# for i in range (0,n+1):
#     print("*"*(n-i), end="")
#     # print(""*i, end="")
#     print(" ")