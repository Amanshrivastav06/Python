# Types of Inheritance 
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance

# MULTIPLE INHERITANCE 

class employee :
    company = "amazone"
    name = "Aman"
    def show(self):
        print(f"the name of employee is {self.name} and the company is {self.company}")

class hacker:
    language = "Hacking Wali"
    def printLanguage(self):
        print(f"atm hack karne ko language {self.language} aani chaiye")

class programmer(employee, hacker):
    company = "Flipcart"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = employee()
b = programmer()

b.show()
b.printLanguage()
b.showLanguage()
