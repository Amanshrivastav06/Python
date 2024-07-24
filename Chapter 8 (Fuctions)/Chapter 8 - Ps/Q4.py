#4. Write a recursive function to calculate the sum of first n natural numbers.

# IT IS USING LOOP
# n = int(input("enter the number: "))
# sum = 0
# i=1
# for i in range(1 , n+1):
#     sum = sum+i
#     i+=1
# print("sum is ", sum)    
          

# # USING BY FUNCTION ye galat hai 
# def sum(n):
#     sum = 0
#     i=1
#     for i in range(1 , n+1):
#         i+=1
#         return sum+i
# n = int(input("enter the number: "))
# print("sum is ", sum(n))   

# USING BY FUNCTION 
def sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

n = int(input("Enter the number: "))
print("Sum is", sum(n))


# USING RECURSIVE FUCTION
'''
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
.
.
sum(n) = 1 + 2 + 3 + 4 .....n-1 + n 
sum(n) = sum(n-1) + n

'''
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# n = int(input("enter the number: "))
# print(f"Sum of first {n} natural number is: {sum(n)}")