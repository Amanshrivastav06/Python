# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def __init__(self , name , salary, language):
        self.name = name 
        self.salary = salary
        self.language = language
       

a = programmer("Aman", 120000, "python")
print(a.name, a.salary, a.language ,a.company)

r = programmer("Rohan", 2000 ,"javascript")
print(r.name, r.salary, r.language, r.company)

        
