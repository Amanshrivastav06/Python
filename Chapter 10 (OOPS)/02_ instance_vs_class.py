# INSTANCE ATTRIBUTE HAVE MORE PRIVILAGE THAN CLASS OR 
# Instance attributes, take preference over class attributes during assignment & retrieval.

class Empolyee:
    salary = 12000000000000000000
    language = "English"

aman = Empolyee
aman.name = "Aman" # this is instance attribute. 
aman.language = "python"
print(aman.salary, aman.language, aman.name)

