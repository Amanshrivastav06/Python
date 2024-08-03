# CONSTRUCTOR - It is a special method in a class used to create and intialize an object of a class and it also invoked automatically 
# when an object of a class is created
# TYPES OF CONSTRUCTOR
# 1. PARAMETERIZED CONSTRUCTOR - YE ARGUMENT LETA HAI 
# 2. DEFAULT CONSTRUCTOR - YE SIRF 1 ARGUMENT LETA HAI (SELF)

class Empolyee:
    salary = 12000000000000000000
    language = "English"

    def __init__(self , name , salary, language): # this __ double underscore are called dunder method. Which is automatically called aur ye SYNTAX HAI CONSTRUCTOR KA
        self.name = name
        self.salary = salary
        self.language = language
        print("Na dhin dhin dhin dhin dhin .. ")
        
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod # use karne se SELF OR DUSRA KEYWORD USE NHI KARNA PDTA.
    def greet():
        print("Good Morning")


aman = Empolyee("Aman", 120000, "python")
# aman.name = "Aman" # this is instance attribute. 
# aman.language = "python"  # iski priority jayada hogi 
print(aman.salary, aman.language, aman.name)