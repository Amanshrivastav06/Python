a = 7 # this is global variable
def f():
    global a # ye global ko change karne ke liye hota hai local me 
    a =6 
    print(a)

f()
print(a)