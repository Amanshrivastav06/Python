#2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class animals:
    pass

class pets(animals):
      pass

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!!")

d = dog()
d.bark()
    
    