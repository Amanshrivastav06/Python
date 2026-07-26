a = 7 # this is global variable
def f():
    global a
    a =6 
    print(a)

f()
print(a)