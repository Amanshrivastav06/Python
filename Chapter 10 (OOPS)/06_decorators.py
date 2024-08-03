# Decorators - is a fuction that takes another fuction as argument and
#  returns a new fuction that modifies the behaviour of the original fuctions.  YE EK FUCTION KO MODIFY KR DETA HAI


def greet(fx):
    def mfx(*args , **kwargs):
        print("Good Morning")
        fx(*args , **kwargs) # ye hello fuction ko execute karega
        print("thanks for using this fuction")
    return mfx

@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a+b)

hello()
# greet(hello)() ye bh same run karega as HELLO() ki trh , @greet ko agr use na krna ho to.

add(2,4 ) 