class empolyee:
    a = 1
    @classmethod # Class method allow to access class atributes first
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
e = empolyee()
e.a = 45 # ye instance variable hai to ye print hoga 

e.show()