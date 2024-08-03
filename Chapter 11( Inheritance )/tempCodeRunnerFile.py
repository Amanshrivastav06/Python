class empolyee:
    a = 1
    @classmethod # Class method allow to access class atributes first
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter