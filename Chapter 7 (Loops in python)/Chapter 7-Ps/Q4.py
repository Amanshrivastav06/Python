#4. Write a program to find whether a given number is prime or not.
num=int(input("Enter the no: "))
# for i in range (2,num):
#     if(num%i)==0:
#         print("Number is not Prime")
#         break
# else:
#     print("Number is prime")

#USING WHILE LOOP
i=2
n=0
while(i<num):
    if(num%i)==0:
        print("Number is not Prime")
        n=1
        break
    i=i+1
else:
    print(f"{num}, is a prime number")


