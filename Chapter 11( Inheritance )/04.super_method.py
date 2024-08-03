class first:
    def __init__(self):
        print("Constructor of first")
    a = "*"

class second(first):
    def __init__(self):
        print("Constructor of second")
    b = "**"

class third(second):
    def __init__(self):
        super().__init__() #  YE ALLOW KRATA HAI APNE SE UPPAR WALE ATTRIBUTE OR CLASS JO ASIGN HAI USE CHALNE ME 
        print("Constructor of third")
    c = "***"

# o = first()
# print(o.a)

# o = second()
# print(o.a , o.b)

o = third()
print(o.a , o.b , o.c)
           