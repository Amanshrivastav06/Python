class first:
    a = "*"

class second(first):
    b = "**"

class third(second):
    c = "***"

o = first()
print(o.a)

o = second()
print(o.a , o.b)

o = third()
print(o.a , o.b , o.c)
           
 