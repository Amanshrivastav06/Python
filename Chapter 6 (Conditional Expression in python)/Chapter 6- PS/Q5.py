#5.Write a program which finds out whether a given name is present in a list or not.
l=["aman","ankit","gaurav","dinesh"]
n=input("enter the Name: ")
if(n in l):
    print(f"{n} is in list")
else:
    print(f"{n} is not in list")