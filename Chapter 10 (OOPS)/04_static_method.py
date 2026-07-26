class Empolyee:
    salary = 12000000000000000000
    language = "English"
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod # use karne se SELF OR DUSRA KEYWORD USE NHI KARNA PDTA.
    def greet():
        print("Good Morning")

aman = Empolyee()
aman.name = "Aman" # this is instance attribute. 
aman.language = "python"  # iski priority jayada hogi 
aman.getInfo()
aman.greet()