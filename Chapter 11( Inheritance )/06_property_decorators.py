class empolyee:
    a = 1
    @classmethod # Class method allow to access class atributes first
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self): # ye name fuc getter ka kam krega
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = empolyee()
e.a = 45 # ye instance variable hai to ye print hoga 

e.name = "Phool Kumari"
print(e.fname, e.lname)
e.show()