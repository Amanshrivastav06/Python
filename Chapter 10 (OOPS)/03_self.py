class Empolyee:
    salary = 12000000000000000000
    language = "English"
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Good Morning")

aman = Empolyee()
aman.name = "Aman" # this is instance attribute. 
aman.language = "python"  # iski priority jayada hogi 
aman.getInfo()
# Empolyee.getInfo(aman) # ye dono same hai fuc ko call karne ke liye.

aman.greet()