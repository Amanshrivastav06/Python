age=int(input("Enter your age: "))
if(age%2==0):
    print("age is even")
    
if(age>=18):
    print("you are Eligible")
elif(age<0):
    print("you are entering wrong age")    
elif(age==0):
    print("you are entering zero which are not valid")    
else:
    print("you are not eligible") 