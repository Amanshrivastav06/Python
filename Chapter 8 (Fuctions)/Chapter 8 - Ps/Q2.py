#2. Write a python program using function to convert Celsius to Fahrenheit. c = 5*(f-32)/9
def fer(f):
   return 5*(f-32)/9
   
f = int(input("Enter the temperature in F: "))
# print(fer(f))
c = fer(f)
print(f"{round(c, 2)}")