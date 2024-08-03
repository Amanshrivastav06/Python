#Inheritance = create a new class from existing class  means parent class se child class banana 

class parent:
    salary = 10000
    language = "english"

hari = parent()
print(f"hari ko english aati hai: {hari.language}")

class children(parent):
    language = "nhi sikha "
hariKaBeta = children()
print(f"hari ka beta ab tak english: {hariKaBeta.language}")



class empolyee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Programmer(empolyee):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = empolyee()
b = Programmer()

print(a.company , b.company)
