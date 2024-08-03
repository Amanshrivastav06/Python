# Class = is a blueprint for creating objects like a student form .. where "Name , Roll no , " are the class and their respective details are objects.
class Empolyee:
    salary = 12000000000000000000
    language = "English"

aman = Empolyee
aman.name = "Aman" # this is instance attribute. 
print(aman.salary, aman.language, aman.name)

gaurav= Empolyee
gaurav.name = "Gaurav"
print(gaurav.salary, gaurav.language, gaurav.name)

# here name is Object or instance attribute and salary and language are class attributes as they directly belong to class

